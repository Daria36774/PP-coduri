import java.io.File
import java.time.LocalDateTime

data class PriceEvent(
    val user: String,
    val oldPrice: Double,
    val newPrice: Double,
    val discount: Double,
    val date: LocalDateTime = LocalDateTime.now()
)

interface PriceObserver {
    fun update(event: PriceEvent)
}

interface DiscountService {
    fun applyDiscount(user: String, password: String, discount: Double)
}

class Product(
    private val name: String,
    private val basePrice: Double
) : DiscountService {

    private var currentPrice = basePrice
    private val observers = mutableListOf<PriceObserver>()

    fun addObserver(observer: PriceObserver) {
        observers.add(observer)
    }

    private fun notifyObservers(event: PriceEvent) {
        observers.forEach { it.update(event) }
    }

    override fun applyDiscount(user: String, password: String, discount: Double) {
        val oldPrice = currentPrice
        currentPrice = basePrice * (1 - discount / 100)

        val event = PriceEvent(
            user = user,
            oldPrice = oldPrice,
            newPrice = currentPrice,
            discount = discount
        )

        notifyObservers(event)

        println("$name: $oldPrice -> $currentPrice")
    }
}

class DiscountProxy(
    private val service: DiscountService,
    private val users: Map<String, String>
) : DiscountService {

    override fun applyDiscount(user: String, password: String, discount: Double) {
        if (users[user] != password) {
            println("User/parola invalide.")
            return
        }

        if (discount < 0 || discount > 100) {
            println("Reducerea trebuie sa fie intre 0 si 100.")
            return
        }

        service.applyDiscount(user, password, discount)
    }
}

class FileLogger(
    private val fileName: String
) : PriceObserver {

    override fun update(event: PriceEvent) {
        File(fileName).appendText(
            "User=${event.user}, data=${event.date}, pret vechi=${event.oldPrice}, reducere=${event.discount}, pret nou=${event.newPrice}\n"
        )
    }
}

fun main() {
    val product = Product("Laptop", 3000.0)
    product.addObserver(FileLogger("log.txt"))

    val proxy: DiscountService = DiscountProxy(
        product,
        mapOf("admin" to "1234")
    )

    print("User: ")
    val user = readLine() ?: ""

    print("Parola: ")
    val pass = readLine() ?: ""

    print("Reducere: ")
    val discount = readLine()?.toDoubleOrNull()

    if (discount != null) {
        proxy.applyDiscount(user, pass, discount)
    } else {
        println("Reducere invalida.")
    }
}
