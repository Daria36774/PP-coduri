from abc import ABC, abstractmethod


class Receiver:
    def __init__(self, name: str, state: str):
        self.name = name
        self.state = state

    def change_state(self, new_state: str) -> None:
        print(f"{self.name}: {self.state} -> {new_state}")
        self.state = new_state

    def __str__(self) -> str:
        return f"Receiver(name={self.name}, state={self.state})"


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class ChangeStateCommand(Command):
    def __init__(self, receiver: Receiver, new_state: str):
        self.receiver = receiver
        self.new_state = new_state
        self.old_state = None

    def execute(self) -> None:
        self.old_state = self.receiver.state
        self.receiver.change_state(self.new_state)

    def undo(self) -> None:
        if self.old_state is not None:
            self.receiver.change_state(self.old_state)


class MakeHappyCommand(ChangeStateCommand):
    def __init__(self, receiver: Receiver):
        super().__init__(receiver, "fericit")


class MakeDesperateCommand(ChangeStateCommand):
    def __init__(self, receiver: Receiver):
        super().__init__(receiver, "disperat")


class MakeCalmCommand(ChangeStateCommand):
    def __init__(self, receiver: Receiver):
        super().__init__(receiver, "linistit")


class Invoker:
    def __init__(self, name: str):
        self.name = name
        self.history = []

    def send_command(self, command: Command) -> None:
        print(f"\n{self.name} trimite {command.__class__.__name__}")
        command.execute()
        self.history.append(command)

    def undo_last(self) -> None:
        if not self.history:
            print("Nu exista comenzi de anulat.")
            return

        command = self.history.pop()
        print(f"\n{self.name} anuleaza {command.__class__.__name__}")
        command.undo()


def main():
    student = Receiver("Maria", "fericit")
    colega = Invoker("Ana")

    print(student)

    colega.send_command(MakeDesperateCommand(student))
    colega.send_command(MakeCalmCommand(student))
    colega.send_command(MakeHappyCommand(student))

    colega.undo_last()

    print(student)


if __name__ == "__main__":
    main()
