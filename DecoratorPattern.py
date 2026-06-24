from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price


class StudentDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.9


class VipDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.75


class PriceCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def final_price(self, price: float) -> float:
        return self.strategy.calculate(price)


def main():
    calculator = PriceCalculator(NoDiscount())

    print(calculator.final_price(100))

    calculator.set_strategy(StudentDiscount())
    print(calculator.final_price(100))

    calculator.set_strategy(VipDiscount())
    print(calculator.final_price(100))


if __name__ == "__main__":
    main()
