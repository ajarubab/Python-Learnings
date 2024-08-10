from abc import ABC, abstractmethod

class Father(ABC):
    
    @abstractmethod
    def show1(self):
        pass
    
    @abstractmethod
    def show2(self):
        pass

class Child(Father):
    def show1(self):
        print("Child class, show1 abstarct method definition")

class GrandChild(Child):
    def show2(self):
        print("Grand Child class, show2 abstarct method definition")


# ch = Child()  #cannot execute because Child class does not having all abstract method defined here
gc = GrandChild()
gc.show1()
gc.show2()