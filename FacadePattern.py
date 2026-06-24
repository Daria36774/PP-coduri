class SubsystemA:
    def operation_a(self):
        print("Operatie A")


class SubsystemB:
    def operation_b(self):
        print("Operatie B")


class SubsystemC:
    def operation_c(self):
        print("Operatie C")


class Facade:
    def __init__(self):
        self.a = SubsystemA()
        self.b = SubsystemB()
        self.c = SubsystemC()

    def operation(self):
        self.a.operation_a()
        self.b.operation_b()
        self.c.operation_c()


def main():
    facade = Facade()
    facade.operation()


if __name__ == "__main__":
    main()
