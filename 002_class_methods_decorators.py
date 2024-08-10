# classes, decorators
class A:
    name = "Raja"
    def __init__(self):
        print("This is init")
    
    def running(sef):
        print("I am runnig")
        
    @classmethod
    def getName(cls):
        return cls.name + " kumar"
    
    @staticmethod
    def staticMessage():
        print("This is static method")
        
    def compare(self, other):
        if(self.name == other.name):
            print("Names are same")
        else:
            print("They are different")

a1 = A()

A.running(a1)
print("-----------")
a1.running()

a1.name = "Ram"
print(A.name)
print(A.getName())
A.staticMessage()

a2 = A()
a2.name = "Ram"
a2.compare(a1)
