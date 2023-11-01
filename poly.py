                   # Method Overrinding....

class A: #Parent
    def Disp(self):
        print("This is parent class method")


class B(A): #Child class
    def Disp(self):
        super().Disp()
        print("This is Child class method")


obj=B()
obj.Disp()