

from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.1415 * (self.radius ** 2)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return (self.side ** 2)

#g = GraphicShape()
c = Circle(2)
print(c.calcArea())
s = Square(4)
print(s.calcArea())