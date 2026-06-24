data class Request(
    val username: String,
    val password: String,
    val role: String
)

abstract class Handler {
    private var next: Handler? = null

    fun setNext(handler: Handler): Handler {
        next = handler
        return handler
    }

    fun handle(request: Request): Boolean {
        if (!check(request)) {
            return false
        }

        return next?.handle(request) ?: true
    }

    protected abstract fun check(request: Request): Boolean
}

class UsernameHandler : Handler() {
    override fun check(request: Request): Boolean {
        if (request.username.isBlank()) {
            println("Username invalid.")
            return false
        }

        println("Username valid.")
        return true
    }
}

class PasswordHandler : Handler() {
    override fun check(request: Request): Boolean {
        if (request.password.length < 4) {
            println("Parola prea scurta.")
            return false
        }

        println("Parola valida.")
        return true
    }
}

class RoleHandler : Handler() {
    override fun check(request: Request): Boolean {
        if (request.role != "admin") {
            println("Rol invalid.")
            return false
        }

        println("Rol valid.")
        return true
    }
}

fun main() {
    val usernameHandler = UsernameHandler()
    val passwordHandler = PasswordHandler()
    val roleHandler = RoleHandler()

    usernameHandler
        .setNext(passwordHandler)
        .setNext(roleHandler)

    val request = Request("daria", "1234", "admin")

    val result = usernameHandler.handle(request)

    println("Rezultat final: $result")
}
