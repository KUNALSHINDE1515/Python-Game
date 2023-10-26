from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def Show(self):
        pass

class Square(Shape):
    def Show(self):
        print("Square has 4 sides")

class Circle(Shape):
    def Show(self):
        print("Circle has circle shape")

s=Square()
s.Show()
c=Circle()
c.Show()
