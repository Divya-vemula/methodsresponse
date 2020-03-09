class Student:
    def person1(self):
        print("this  student function")
class Test(Student):
    def person1(self):
        print("this test function")
obj = Test()
obj.person1()