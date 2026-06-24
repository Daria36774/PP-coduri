class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.file_name = "app.log"
        return cls._instance

    def log(self, message: str) -> None:
        with open(self.file_name, "a") as file:
            file.write(message + "\n")


def main():
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Primul mesaj")
    logger2.log("Al doilea mesaj")

    print(logger1 is logger2)


if __name__ == "__main__":
    main()
