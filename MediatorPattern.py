from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague_a = None
        self.colleague_b = None

    def notify(self, sender, event: str) -> None:
        if event == "A":
            print("Mediatorul a primit eveniment de la A si notifica B.")
            self.colleague_b.receive("Mesaj de la A")

        if event == "B":
            print("Mediatorul a primit eveniment de la B si notifica A.")
            self.colleague_a.receive("Mesaj de la B")


class Colleague:
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator

    def send(self, event: str) -> None:
        print(f"{self.name} trimite eveniment {event}")
        self.mediator.notify(self, event)

    def receive(self, message: str) -> None:
        print(f"{self.name} primeste: {message}")


def main():
    mediator = ConcreteMediator()

    a = Colleague("A", mediator)
    b = Colleague("B", mediator)

    mediator.colleague_a = a
    mediator.colleague_b = b

    a.send("A")
    b.send("B")


if __name__ == "__main__":
    main()
