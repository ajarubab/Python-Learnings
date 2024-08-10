#polymorphism using duck typing
class Candidate1:
    def Qualifications(self):
        print("10th passed")
        print("12th passed")

class Candidate2:
    def Qualifications(self):
        print("10th passed")
        print("12th passed")
        print("Diploma in CSE")

class Candidate3:
    def Qualifications(self):
        print("10th passed")
        print("12th passed")
        print("Diploma in CSE")
        print("Btech in IT")

class Selection:
    def selectedCandidate(self,person):
        person.Qualifications()

# person = Candidate1()
# person = Candidate2()
person = Candidate3()

s1 = Selection()
s1.selectedCandidate(person)