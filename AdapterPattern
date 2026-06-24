import java.io.File

interface Target {
    fun execute(data: Any?, fileName: String)
}

class Adaptee {
    fun specificWrite(fileName: String, lines: List<String>) {
        File(fileName).appendText(lines.joinToString("\n", postfix = "\n"))
    }
}

class Adapter(
    private val adaptee: Adaptee
) : Target {

    override fun execute(data: Any?, fileName: String) {
        val lines = when (data) {
            null -> listOf("null")

            is Map<*, *> -> data.map { entry ->
                "${entry.key} -> ${entry.value}"
            }

            is Iterable<*> -> data.map { element ->
                element.toString()
            }

            is Array<*> -> data.map { element ->
                element.toString()
            }

            else -> listOf(data.toString())
        }

        adaptee.specificWrite(fileName, lines)
    }
}

class Application(
    private val target: Target
) {
    fun run(data: Any?, fileName: String) {
        target.execute(data, fileName)
    }
}

fun main() {
    val fileName = "output.txt"
    File(fileName).writeText("")

    val adaptee = Adaptee()
    val adapter = Adapter(adaptee)
    val app = Application(adapter)

    app.run(100, fileName)
    app.run("Ana", fileName)
    app.run(listOf(1, 2, 3), fileName)
    app.run(mapOf("mere" to 5, "pere" to 3), fileName)

    println("Date scrise in $fileName")
}
