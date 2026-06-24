interface Service {
    fun operation(username: String, password: String, value: Double)
}

class RealService : Service {
    override fun operation(username: String, password: String, value: Double) {
        println("Operatie reala executata cu valoarea $value")
    }
}

class ServiceProxy(
    private val realService: Service,
    private val users: Map<String, String>
) : Service {

    override fun operation(username: String, password: String, value: Double) {
        if (users[username] != password) {
            println("Acces respins.")
            return
        }

        if (value < 0) {
            println("Valoare invalida.")
            return
        }

        realService.operation(username, password, value)
    }
}

fun main() {
    val users = mapOf("admin" to "1234")
    val realService = RealService()
    val proxy: Service = ServiceProxy(realService, users)

    proxy.operation("admin", "1234", 10.0)
    proxy.operation("admin", "wrong", 10.0)
}
