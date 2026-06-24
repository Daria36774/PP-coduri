from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def show(self, level: int = 0) -> None:
        pass


class Leaf(Component):
    def __init__(self, name: str):
        self.name = name

    def show(self, level: int = 0) -> None:
        print("  " * level + self.name)


class Composite(Component):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def show(self, level: int = 0) -> None:
        print("  " * level + self.name)

        for child in self.children:
            child.show(level + 1)


def main():
    root = Composite("Root")

    file1 = Leaf("file1.txt")
    file2 = Leaf("file2.txt")

    folder = Composite("Folder")
    folder.add(Leaf("file3.txt"))

    root.add(file1)
    root.add(file2)
    root.add(folder)

    root.show()


if __name__ == "__main__":
    main()
