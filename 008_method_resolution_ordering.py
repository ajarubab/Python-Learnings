# use of super method(method overriding) and method resolution ordering (MRO)
class A:
    def __init__(self) -> None:
        print("into init of class A")
    
    def action1(self):
        print("into the action A-1")
    def action2(self):
        print("into the action 2")

class B:
    def __init__(self) -> None:
        # super().__init__()
        print("into init of class B")
    
    def action1(self):
        print("into the action B-1")
    def action4(self):
        print("into the action 4")

class C(A,B):
    def __init__(self) -> None:
        super().__init__()
        print("into init of class C")

# a1 = A()
# b1 = B()
c1 = C()