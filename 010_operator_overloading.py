# operator overloading in polymorphism
class A:
    def area(self,l=None,b=None):
        if(l!=None and b!=None):
            print("The Area is rectangle", l * b)
        elif(b!=None):
            print("Area of circle is ", 3.14*b*b)
        else:
            print("Nothing to display") 
    
        
obj = A()
obj.area()
obj.area(12,13)
obj.area(None, 14)