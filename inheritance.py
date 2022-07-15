class Parent:
    def func1(self):
        print("This is the function1")

class Child(Parent):
    def func2(self):
        super().func1()

ob = Child()
ob.func2()        