class Student:
    def mark1(self):
        print("score in tamil ")
class Exam(Student):
    def mark2(self):
        print("score in english")
class Total(Student):
    def mark3(self):
        print("score in computer")
obj = Exam()
obj1 = Total()
obj.mark1()
obj.mark2()
