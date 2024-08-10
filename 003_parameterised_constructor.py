# parameterised init and value modification
class A:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def action(self):
        self.age = self.age + 10
        print(self.name," is of ",self.age)
    
a1 = A("Raja", 22)
a2 = A("Ram", 25)

a1.action()
a2.action()