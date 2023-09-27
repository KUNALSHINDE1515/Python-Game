      #python DEfault Contructor #

class K:
    name="kunal Shinde"
    age=20
    def __init__(self):
        address="Pune"
        print(self.name," ",address)
    def show(self):
        print(self.age)

obj=K()
obj.show()
