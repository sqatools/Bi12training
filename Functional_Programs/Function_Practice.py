"""
def function_name():
    code
"""

def addition():
    num1 = 20
    num2 = 30
    print(num1+num2)

#addition()

# Provide parameter/arguments

def addition2(num1, num2):
    print("Addition :", num1 + num2)

# 1. Pass by value
#addition2(50, 70)

# 2. Pass by reference
x = 40
y = 70
#addition2(x, y)
p = 90
q = 50
#addition2(p, q)
#addition2('Python', 'Programming')

# default value to the parameters

def multiplication(num1, num2=50):
    print("Num1:", num1)
    print("Num2:", num2)
    print("Multiplication :",  num1*num2)


# case1: if parameter has default value then no need to mention
# while calling the function
# multiplication(6) # num1 = 6, num2 = 50

# case2 : If we want change the default value of the param then we have
# mention while calling the function.
p1 , q1 = 70, 5
#multiplication(p1, q1)  # num1 = p1 = 70, num2 = q1 = 5

# case3 : provide value to the params to their name
#multiplication(num1=50, num2=40)

# case 4: if we want to change the order of param then we have to provide
# param names while calling the function.
#multiplication(num2=70, num1=4)

# *args : provide list of values to the function

def square_of_all_numbers(*args):
    for data in args:
        print(data, "|", data**2)


#square_of_all_numbers(3, 6, 8, 2, 9, 12)


def cube_of_all_numbers(num1, x,  y, z, *args, num2=50, num3=60, num4=70):
    print("Num1:", num1, x, y, z)
    print([p**2 for p in num1])
    print("Num2:", num2)
    print("Num3:", num3)
    print("Num4:", num4)
    print("Args:", args)
    for data in args:
        print(data, "|", data**3)

#cube_of_all_numbers(23, 56, 87, 2, 9, 2, 5, 1, 6)
#cube_of_all_numbers('Python', 56, 87, 2, 9, 2, 5, 1, 6, num2=30)
#cube_of_all_numbers([5, 8, 2, 9], 56, 87, 2, 9, 2, 5, 1, 6, num2=30)
#cube_of_all_numbers([5, 8, 2, 9], 56, 87, 2, None, num2=30)
#____________________________________________
# **kwargs : defined param values in key values format

def employee_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)

#employee_info(name='Rahul', email='Rahul@gmail.com', mobile=4567)


def login(**kwargs):
    db_username = 'Amar'
    db_password = 'P@ssw0rd'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Access denied, wrong username password")

#login(username='Amar', password='P@ssw0rd')
#login(username='Amar1', password='P@ssw0rd1')


def pramod_data(*args):
    print(args)
    for data in args:
        print(data, ":", data**2)

#pramod_data(5, 3, 8, 20, 50, 45)