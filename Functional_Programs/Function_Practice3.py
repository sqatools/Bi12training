def addition(num1, num2):
    output = num1 + num2
    return output

def multiplication(num1, num2):
    return num1*num2

# num1 = 50
# num2 = 60
# num3 = 7
# var1 = addition(num1, num2)
# output = multiplication(var1, num3)
# print(output)

# Documentation of the function

#str1 = "Hello"
#str1.title()
def provide_default():
    return 5

def get_factorial(num: int):
    """ this function will provide and factorial of any given number
    factorial example: factorial of 5 means : 5*4*3*2*1
    :param num: this is user input to get
    its factorial
    :return:
    """
    if num == 0:
        num = provide_default()
    fact = 1
    for i in range(num, 0, -1):
        fact = fact*i
    return fact

print(get_factorial(0))
#print(get_factorial('Hello'))

#print(get_factorial.__doc__)

"""
-> Defined function  with params
-> Call function and provide values with "call by ref" or "call by value"
-> Default value to the parameters
-> Use of *args
-> Use of **kwargs
-> Scope of the function variable local, global, non local
-> call function outside of the module.
-> provide return type to the the function with return keyword
-> Add documentation to the function.
-> Add type of value to the function
-> Create child function, means function inside the function. 
-> calling function inside a function.
"""

# Default value to the parameters

def function1(num1, num2=50):
    print("num1:", num1)
    print("num2:", num2)
# num2 with default value
#function1(30)
# num2 with new values
#function1(30, 100)

#  Use of *args
def function2(*args):
    print(args)
    for var in args:
        print(var)

#function2(4, 6, 2, 7, 8, 9, 'Python', [5, 7, 8], {'a': 45, 'b': 456})
#list2 = [6, 7, 2.3, 'hello']
#function2(list2)

# use of **kwargs
def functions4(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)

#functions4(name='Pramod', email='pramod@gmail.com', phone=34566576)

def institude(marks):
    result_dict ={}
    def get_6_th_result():
        input = marks['6th']
        grade_6th = {}
        result_dict['6th'] = grade_6th

    def get_7_th_result():
        input = marks['7th']
        grade_7th = {}
        result_dict['7th'] = grade_7th

    get_6_th_result()
    get_7_th_result()
    return result_dict


#result = institude("student_marks")