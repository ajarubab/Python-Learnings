# Multiple Inheritance
class A:
    def work1(self):
        print("This is work 1")
    def work2(self):
        print("This is work 2")

class B:
    def work3(self):
        print("This is work 3")
    def work4(self):
        print("This is work 4")
    
class C(A,B):
    def work5(self):
        print("This is work 5")
    def work6(self):
        print("This is work 6")

c1 =  C()

c1.work1()
c1.work2()
c1.work3()
c1.work4()
c1.work5()
c1.work6()
