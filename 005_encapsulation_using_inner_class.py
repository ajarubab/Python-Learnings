# Inner Classes
class A:
    def __init__(self, name, rollNo) -> None:
        self.name = name
        self.rollNo = rollNo
        self.b = self.B()
    
    def show(self):
        print(self.name, self.rollNo)
        self.b.show()
    
    class B:
        def __init__(self) -> None:
            self.brand = "HP"
            self.ram = 8
            self.cpu = 4
        
        def show(self):
            print(self.brand, self.ram, self.cpu)
    
s1 = A("raja", 22)
s2 = A("raju", 25)

s1.show()
s2.show()