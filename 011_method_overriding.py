# method overriding
class A:
    def show(self):
        print("In A class Show")

class B(A):
    def show(self):
        # super().show()
        print("In B class Show")

obj = B()
obj.show()