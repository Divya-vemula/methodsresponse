class Class1:
    def person(self):
        print("In Class1")


class Class2(Class1):
    def person(self):
        print("In Class2")


class Class3(Class1):
    def person(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.person()