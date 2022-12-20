"""
class : class is nothing but a blueprint of any object, where we define all the properties, attributes
that we can through the object.
object : Object is an entity through which we can access the property of the class.
method/class method/ instances method/ static method

constructor : constructor initialize the memory of the object
def __init__

1. default constructor : the constructor which initial the memory by default when ever we create object
                    of the class
2. Parameterize constructor :

Inheritance
Polymorphism
Abstraction
Encapsulation/Data hiding
Destructor
"""

class A:
    # parametrize constructor
    def __init__(self, name, age):
        self.user_name = name  # Instance variable
        self.user_age = age    # Instance variable

    # Method / Object Method / Instance Method
    def print_greeting(self):
        print("Good Morning")

    def show_person(self):
        print(f"name : {self.user_name}")
        print(f"age : {self.user_age}")

    def new_function(self, msg):
        print(msg)


# obj = A()
# obj.print_greeting()
# print(obj.__module__)

if __name__ == '__main__':
    obj = A('Amar', 25)
    #obj.new_function()
    A.new_function(obj, "Good Morning")
    print(obj.user_age)
    print(obj.__module__)
    print(__name__)
    print(obj.__getattribute__('user_age'))
    obj.__setattr__('user_age', 50)
    print(obj.user_age)

"""
What is self? : Self is nothing but object of the class.
when we call any method with the object, then enternaly that object is first parameter for the method. 
"""





"""
Class school -> school name, city, address, total department, show_all_details
     -> name
     -> address
     -> city
     -> department
     -> show_All_details

Class car -> name, company, prize, model
      -> name method
      -> company method
      -> prize method
      -> model method
      -> show all details
      
Class Company -> name, IT, HR, Admin, Finance
     -> create methods as per parameters 
"""