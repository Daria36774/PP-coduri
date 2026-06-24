from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Produs A"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Produs B"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> None:
        product = self.factory_method()
        print(product.operation())


class CreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class CreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


def main():
    creator: Creator = CreatorA()
    creator.some_operation()

    creator = CreatorB()
    creator.some_operation()


if __name__ == "__main__":
    main()
