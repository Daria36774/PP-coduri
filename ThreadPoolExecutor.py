from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
import time


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, message: str):
        self.message = message

    def execute(self):
        time.sleep(1)
        print(self.message)


class CommandExecutor:
    def __init__(self, max_workers: int):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, command: Command):
        return self.executor.submit(command.execute)

    def shutdown(self):
        self.executor.shutdown()


def main():
    executor = CommandExecutor(max_workers=3)

    commands = [
        PrintCommand("Comanda 1"),
        PrintCommand("Comanda 2"),
        PrintCommand("Comanda 3")
    ]

    futures = []

    for command in commands:
        futures.append(executor.submit(command))

    for future in futures:
        future.result()

    executor.shutdown()


if __name__ == "__main__":
    main()
