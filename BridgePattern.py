from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> None:
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> None:
        print(f"Desenez cerc vectorial cu raza {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> None:
        print(f"Desenez cerc raster cu raza {radius}")


class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> None:
        self.renderer.render_circle(self.radius)


def main():
    vector_circle = Circle(VectorRenderer(), 5)
    raster_circle = Circle(RasterRenderer(), 10)

    vector_circle.draw()
    raster_circle.draw()


if __name__ == "__main__":
    main()
