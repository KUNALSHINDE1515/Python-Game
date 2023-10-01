                                #  Python Hierarchical inheritance #

class Father:
    surname="Shinde(Deshmukh)"
    def Show(self):
        print("My Surname Is ",self.surname)

class Son1(Father):
    def Disp(self):
        print("My Name is KUNAl",self.surname)

class SOn2(Father):
    def Disp(self):
        print("My name is Pranali",self.surname)


s1=Son1()
s2=SOn2()

s1.Disp()
s2.Disp()