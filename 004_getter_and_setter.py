# Getter and Setter Method
class A:

    def setValue(self):
        self.num1 = 15
        self.num2 = 25
        self.num3 = 35
    
    def getValue(self):
        print(self.num1, self.num2, self.num3)
    
a1= A()
a1.setValue()
a1.getValue()
        