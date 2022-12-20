"""
class : class is nothing but, the blueprint to design a object
object : object is something through we can access the all the properties and attribute of the class
method : method is class member through which we can decide the functionality of the class and set its property.
constructor : constructor which initialize the memory of the object.
             -> default constructor
            -> parametize constructor
inheritance : one class aquire the property of another class in knows as inheritance
             -> single inheritance (class A -> Class B)
             -> multiple level inheritance (class A -> Class B -> Class C)
             -> Multiple Inheritance (class A -> Class B,  Class C -> Class B)
polymorphism : when one attribute perform multiple operation, then it is known as polymorphism
data hiding/encapsulation
abstractions
"""

"""
# Class declaration
class car:
    

    # Method
    def car_name(self):
        print("This is Baleno Car")

    # Method
    def number_of_wheels(self):
        print("Car has four wheels")


obj1 = car()
obj1.car_name()
obj1.number_of_wheels()

obj2 = car()
obj3 = car()
obj4 = car()

obj4.car_name()
"""

"""
#####################
# Class declaration
class car:
    # class variable
    car_model = '2022'

    def __init__(self, car_name,  car_company, car_price):
        self.car_name = car_name # instance variable
        self.car_comp = car_company
        self.price =  car_price

    # instance method/object method
    def show_car_name(self):
        print(f"car_name :{self.car_name}")

    # instance method/object method
    def number_of_wheels(self):
        print("Car has four wheels")

    # instance method/object method
    def show_car_company(self):
        print("company name :", self.car_comp)


obj1 = car('altroz', 'TATA', '10 Lac')
obj1.show_car_name()
obj1.show_car_company()
print(obj1.car_model)
"""


##############################################
# single inheritance
# parent class
"""
class A:
    def method_a1(self):
        print("class A1 method")

    def method_a2(self):
        print("class A2 method")
        
       
# child 
class B(A):
    def method_b1(self):
        print("class B1 method")

    def method_b2(self):
        print("class B2 method")
        

objb = B()
objb.method_b1()
objb.method_a1()
"""

"""
# Multi level inheritance

class A:
    def method_a1(self):
        print("class A1 method")

    def method_a2(self):
        print("class A2 method")


# child
class B(A):
    def method_b1(self):
        print("class B1 method")

    def method_b2(self):
        print("class B2 method")

class C(B):
    def method_c1(self):
        print("class C1 method")

    def method_c2(self):
        self.method_a1()
        self.method_b1()
        print("class C2 method")


objc = C()
objc.method_c2()
"""

# Multiple Inheritance
"""
class A:
    def method_a1(self):
        print("class A1 method")

    def method_a2(self):
        print("class A2 method")


# child
class B:
    def method_b1(self):
        print("class B1 method")

    def method_b2(self):
        print("class B2 method")

class C(A, B):
    def method_c1(self):
        print("class C1 method")

    def method_c2(self):
        self.method_a1()
        self.method_b1()
        print("class C2 method")


objc = C()
objc.method_c1()

objb = B()
objb.method_b1()

obja = A()
obja.method_a1()

"""


# Polymorphism
# Method Overriding : when two class have same method name,
# then prefrence will be given the class which object is being created.

# Method overloading: Python does not support it.
# operator overloading : one plus operator can add int, float, string, list, tuple

"""
class A:
    def method_a1(self):
        print("class A1 method")

    def method_a2(self):
        print("class A2 method")

    def shows_msg(self):
        print("A We are learning Python")


# child
class B(A):
    def method_b1(self):
        print("class B1 method")

    def method_b2(self):
        print("class B2 method")

    def shows_msg(self):
        print("B We are learning Python")

    def method_b2(self, name):
        print(f"B We are learning Python :{name}")

objb = B()
objb.shows_msg()
objb.method_b2()
"""

# Data Hiding and Incapsulation: we can pretend to hide the data using single underscore and double underscore
# -> if any data specified with singel/double as prefix, then those data will not show in the suggestion.
# -> single underscore data we can access direcly with name, only it wont be visible in suggestion  list
# -> Double underscore data we can access with patter (obj._classname__data)with name, it wont be visible in suggestion list
class A:
    vara = 'Mumbai'
    _varb = "Pune"
    __varc = "Delhi"

    def method_a1(self):
        print("class A1 method")

    def _method_a2(self):
        print("class A2 method")

    def __shows_msg(self):
        print("A We are learning Python")


obj = A()

obj._method_a2()

obj._A__shows_msg()


print(dir(obj))

str1= "Hello"

str1.upper()