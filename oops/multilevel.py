class Student:
    def getStudent(self):
        self.name=input("name:")
        self.age=input("age:")
        self.gender=input("gender:")
    def getMarks(self):
        self.stuClass=input("class:")
        print("enter the marks ")
        self.math=int(input ("math:"))
        self.eng = int(input("eng:"))
        self.computer = int(input("computer:"))
    class marks(test):
        def display(self):
            print("\n\nName:",self.name)
            print("Age:",self.age)
            print("Gender:", self.gender)
            print("study in:",self.stuClass)
            print("TotalMarks:",self.math+self.eng+self.computer)
        m1=marks()
        m1.getStudent()
        m1.getMarks()
        m1.display()