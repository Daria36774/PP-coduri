from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self) -> None:
        self.read_data()
        self.transform_data()
        self.save_data()

    @abstractmethod
    def read_data(self) -> None:
        pass

    @abstractmethod
    def transform_data(self) -> None:
        pass

    @abstractmethod
    def save_data(self) -> None:
        pass


class CsvProcessor(DataProcessor):
    def read_data(self) -> None:
        print("Citesc date CSV.")

    def transform_data(self) -> None:
        print("Transform date CSV.")

    def save_data(self) -> None:
        print("Salvez date CSV.")


class JsonProcessor(DataProcessor):
    def read_data(self) -> None:
        print("Citesc date JSON.")

    def transform_data(self) -> None:
        print("Transform date JSON.")

    def save_data(self) -> None:
        print("Salvez date JSON.")


def main():
    processor: DataProcessor = CsvProcessor()
    processor.process()

    processor = JsonProcessor()
    processor.process()


if __name__ == "__main__":
    main()
