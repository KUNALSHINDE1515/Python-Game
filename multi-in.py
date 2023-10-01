                            # Pyhon MultiLevel Inheritance........#

class Father:
    surname="Shinde"
class chlid1(Father):
    def show(self):
        print("Kunal",self.surname)
class child2(chlid1):
    def Disp(self):
        print("Pranali",self.surname)

C=chlid1()
C.show()

c=child2()
c.Disp()