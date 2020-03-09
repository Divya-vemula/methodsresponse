class Base:
    def __init__(self):
        self.a = "divya"
        self.__c = "vemula"
# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__a)
obj1 = Base()
print(obj1.a)