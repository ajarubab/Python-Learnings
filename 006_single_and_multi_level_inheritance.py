# Single level Inheritance and Multi level Inheritance
class A:
    def work1(self):
        print("this is Work 1")
    def work2(self):
        print("this is Work 2")

a1, a2 = A(), A()

# a1.work1()
# a2.work2()

class B(A):
    def work3(self):
        print("this is Work 3")
    def work4(self):
        print("this is Work 4")

# b1, b2 = B(), B()

# b1.work1()
# b1.work2()
# b1.work3()
# b1.work4()

class C(B):
    def work5(self):
        print("this is Work 5")
    def work6(self):
        print("this is Work 6")

c1, c2 = C(), C()

c2.work1()
c2.work2()
c2.work3()
c2.work4()
c2.work5()
c2.work6()