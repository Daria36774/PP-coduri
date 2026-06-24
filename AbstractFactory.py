from abc import ABC, abstractmethod
import tkinter as tk


class Button(ABC):
    @abstractmethod
    def label(self) -> str:
        pass


class RomanianButton(Button):
    def label(self) -> str:
        return "Apasa"


class EnglishButton(Button):
    def label(self) -> str:
        return "Click"


class FrenchButton(Button):
    def label(self) -> str:
        return "Cliquez"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass


class RomanianFactory(GUIFactory):
    def create_button(self) -> Button:
        return RomanianButton()


class EnglishFactory(GUIFactory):
    def create_button(self) -> Button:
        return EnglishButton()


class FrenchFactory(GUIFactory):
    def create_button(self) -> Button:
        return FrenchButton()


class FactoryProducer:
    @staticmethod
    def get_factory(language: str) -> GUIFactory:
        language = language.lower()

        if language == "ro":
            return RomanianFactory()

        if language == "en":
            return EnglishFactory()

        if language == "fr":
            return FrenchFactory()

        raise ValueError("Limba nesuportata.")


class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory

    def run(self):
        button_model = self.factory.create_button()

        root = tk.Tk()
        root.title("Abstract Factory")

        button = tk.Button(root, text=button_model.label(), width=20)
        button.pack(padx=30, pady=30)

        root.mainloop()


def main():
    language = input("Limba ro/en/fr: ")

    try:
        factory = FactoryProducer.get_factory(language)
        app = Application(factory)
        app.run()
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
