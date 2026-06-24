from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def process(self, order):
        pass

    @abstractmethod
    def deliver(self, order):
        pass

    @abstractmethod
    def cancel(self, order):
        pass


class NewOrder(OrderState):
    def process(self, order):
        print("Comanda a fost procesata.")
        order.state = ProcessedOrder()

    def deliver(self, order):
        print("Nu se poate livra direct.")

    def cancel(self, order):
        print("Comanda noua a fost anulata.")
        order.state = CancelledOrder()


class ProcessedOrder(OrderState):
    def process(self, order):
        print("Comanda este deja procesata.")

    def deliver(self, order):
        print("Comanda a fost livrata.")
        order.state = DeliveredOrder()

    def cancel(self, order):
        print("Comanda procesata a fost anulata.")
        order.state = CancelledOrder()


class DeliveredOrder(OrderState):
    def process(self, order):
        print("Comanda este deja livrata.")

    def deliver(self, order):
        print("Comanda este deja livrata.")

    def cancel(self, order):
        print("Nu se mai poate anula.")


class CancelledOrder(OrderState):
    def process(self, order):
        print("Comanda este anulata.")

    def deliver(self, order):
        print("Comanda este anulata.")

    def cancel(self, order):
        print("Comanda este deja anulata.")


class Order:
    def __init__(self):
        self.state = NewOrder()

    def process(self):
        self.state.process(self)

    def deliver(self):
        self.state.deliver(self)

    def cancel(self):
        self.state.cancel(self)


def main():
    order = Order()

    order.deliver()
    order.process()
    order.deliver()
    order.cancel()


if __name__ == "__main__":
    main()
