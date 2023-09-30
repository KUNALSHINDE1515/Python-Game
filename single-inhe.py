            #  Single inh Python

class A:
     nam1=int(input("Enter 1St Number: "))
     nam2=int(input("Enter 2nd Number: "))

     def Add(self):
          print("ADDition: ",self.nam1+self.nam2)
     def Sub(self):
          print("sub: ",self.nam1-self.nam2)


class B(A):
     def multi(self):
          print("Multi is",self.nam1*self.nam2)

     def div(self):
          print("Multi is",self.nam1/self.nam2)

obj=B()
obj.Add()
obj.Sub()
obj.multi()
obj.div()