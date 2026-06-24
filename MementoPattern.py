class Memento:
    def __init__(self, state: str):
        self.state = state


class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text: str) -> None:
        self.text += text

    def save(self) -> Memento:
        return Memento(self.text)

    def restore(self, memento: Memento) -> None:
        self.text = memento.state

    def show(self) -> None:
        print(self.text)


class History:
    def __init__(self):
        self.states = []

    def push(self, memento: Memento) -> None:
        self.states.append(memento)

    def pop(self) -> Memento:
        return self.states.pop()


def main():
    editor = Editor()
    history = History()

    editor.write("Ana ")
    history.push(editor.save())

    editor.write("are mere.")
    editor.show()

    editor.restore(history.pop())
    editor.show()


if __name__ == "__main__":
    main()
