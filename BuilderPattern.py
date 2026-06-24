class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage})"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def build(self) -> Computer:
        return self.computer


def main():
    computer = (
        ComputerBuilder()
        .set_cpu("i7")
        .set_ram("16GB")
        .set_storage("512GB SSD")
        .build()
    )

    print(computer)


if __name__ == "__main__":
    main()
