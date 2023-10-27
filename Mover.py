        #....Method Overloading.....#

class A:
    # def Show(self):
    #     print("WElcome BAck")


    # def Show(self,firstname=''):
    #     print("wElcome",firstname)


    def Show(self,firstname='',lastname=''):
        print("welcome",firstname,lastname)


obj=A()
obj.Show()
obj.Show("kunal")
obj.Show("KUanl","Shinde")