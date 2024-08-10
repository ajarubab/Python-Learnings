class A:
    pass

a1 = A()
a2 = A()

print(id(a1), id(a2))

class B:
    
    def __init__(self) -> None:
        self.name = "Ram"
        self.age = 25
    
b1, b2 = B() , B()

print(b1.name, b2.name)

b1.name = "Siya"

print(b1.name,b2.name)