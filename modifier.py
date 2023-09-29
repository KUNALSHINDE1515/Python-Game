class A:
    a=10 #public
    _b=20 #protected
    __c=None #private   

    print(a," ",_b," ",__c)
    
    def Add(self):
        self.__c=self.a+self._b
        print("Addition : ",self.__c)

# obj=A()
# obj.Add()
# print(obj.a)
# print(obj._b)
# print(obj.__c)

class B(A):  #child
    def show(self):
        print(self.a)
        print(self._b)
        # print(self.__c)

obj=B()
obj.show()
