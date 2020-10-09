#Classes and object
class Person:
    age = 10
    def greet(self):
        print('Hello')

harry=Person()
harry.greet()

#Constructors
class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    def display(self):
        print("ID:",self.id," Name: " ,self.name)

emp1 = Employee("David", 102)
emp1.display()

# Single Inheritance
class parent:
    def first(self):
        print("First function")
class child(parent):
    def second(self):
        print("Second function")

ob=child()
ob.first()
ob.second()

#Multiple inheritance
class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
    def func2(self):
        print("this is function 2")
class Child(Parent, Parent2):
    def func3(self):
        print("this is function 3")

ob = Child()
ob.func1()
ob.func2()
ob.func3()

#Multilevel inheritance
class Parent:
    def func1(self):
        print("this is function 1")
class Child(Parent):
    def func2(self):
        print("this is function 2")
class Child2(Child):
    def func3(self):
        print("this is function 3")

ob = Child2()
ob.func1()
ob.func2()
ob.func3()

#Hierarchical inheritance
class Parent:
    def func1(self):
        print("this is function 1")
class Child(Parent):
    def func2(self):
        print("this is function 2")
class Child2(Parent):
    def func3(self):
        print("this is function 3")

ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()

#Hybrid inheritance
class Parent:
    def func1(self):
        print("this is function one")
class Child1(Parent):
    def func2(self):
        print("this is function 2")
class Child2(Parent):
    def func3(self):
        print(" this is function 3")
class Child3(Child1,Parent):
    def func4(self):
        print(" this is function 4")

ob = Child3()
ob.func1()
ob.func2()