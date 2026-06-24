data class Event(
    val oldValue: Double,
    val newValue: Double,
    val message: String
)

interface Observer {
    fun update(event: Event)
}

interface Subject {
    fun addObserver(observer: Observer)
    fun removeObserver(observer: Observer)
    fun notifyObservers(event: Event)
}

class ConcreteSubject(
    initialValue: Double
) : Subject {

    private var value: Double = initialValue
    private val observers = mutableListOf<Observer>()

    fun changeValue(newValue: Double) {
        val oldValue = value
        value = newValue

        val event = Event(
            oldValue = oldValue,
            newValue = newValue,
            message = "Valoarea s-a modificat"
        )

        notifyObservers(event)
    }

    override fun addObserver(observer: Observer) {
        observers.add(observer)
    }

    override fun removeObserver(observer: Observer) {
        observers.remove(observer)
    }

    override fun notifyObservers(event: Event) {
        for (observer in observers) {
            observer.update(event)
        }
    }
}

class ConsoleLogger : Observer {
    override fun update(event: Event) {
        println("${event.message}: ${event.oldValue} -> ${event.newValue}")
    }
}

fun main() {
    val subject = ConcreteSubject(100.0)
    val logger = ConsoleLogger()

    subject.addObserver(logger)

    subject.changeValue(80.0)
    subject.changeValue(60.0)
}
