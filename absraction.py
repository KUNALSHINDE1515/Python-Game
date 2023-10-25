#      Python Abstraction

from abc import ABC,abstractmethod

class Car(ABC):
    def Show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def Speed(self):
        pass
class Maruti(Car):
    def Speed(self):
        print("Speed is 100km/h")

class Mahindra(Car):
    def Speed(self):
        print("Spedd is 150km/h")

obj=Maruti()
obj.Show()
obj.Speed()
obj2=Mahindra()
obj2.Show()
obj2.Speed