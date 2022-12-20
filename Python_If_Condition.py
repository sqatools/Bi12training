"""
if condition:
    code
else:
    code

"""
key = False

if key:
    print("Door Open Successfully")
else:
    print("Can not open door, key is not matching")








"""
conditional Operator

== : equal to operator
!= : not equal to 
> : greater than
< : less than
>= : greater than equal to
<= : less than equal to
% : remainder operator
"""

"""
Nested if condition

if condition
   code
   if condition
       code
   else:
       code
else:
    code
"""

num = 51
if num%10 == 0:
    print("This number can be divide by 10")
    if num%3 == 0:
        print("Number can also divide by 3")
    else:
        print("Number can not divide by 3")
else:
    print("Can not divide This number by 10")
"""
num = 30
This number can be divide by 10
Number can also divide by 3
num = 50
This number can be divide by 10
Number can not divide by 3
num = 51
Can not divide This number by 10
"""

"""
if condition:
    code
elif condition:
    code
else:
     code
"""

num = 51

if num%2 == 0:
    print("Its divisible by 2")
elif num%5 == 0:
    print("Its divisible by 5")
else:
    print("Can not divide by 2 or 5")

"""
Logical Operator AND , OR

AND : All the condition should be true:
condition1 and condition2

TRUE  and  TRUE :  TRUE
FALSE and  TRUE :  FALSE
TRUE  and  FALSE : FALSE
FALSE and  FALSE : FALSE

OR : Anyone condition can be true
condition1 or condition2

TRUE or TRUE : TRUE
TRUE or FALSE : TRUE
FALSE or TRUE : TRUE
FALSE or FALSE : FALSE
"""

marks = 39
"""
if marks > 40 and marks < 50:
    print("You passed with third grade")
else:
    print("condition is not mathing")
"""
print("_"*50)
if marks > 40 or marks < 50:
    print("You passed with third grade")
else:
    print("condition is not mathing")


# Write python program to check student grade as per marks obtains

marks = int(input("Please enter student marks:"))
if marks <= 100:
    if marks > 30 and marks <= 40:
        print("Student passed with lowest grade")
    elif marks > 40 and marks <= 50:
        print("Student passed with second grade")
    elif marks > 50 and marks <= 60:
        print("Student passed with First grade")
    elif marks > 60 and marks <= 80:
        print("Student passed with A grade")
    elif marks > 80 and marks <= 100:
        print("Student passed with A++ grade")
    else:
        print("Student Failed in the exams")
else:
    print("Invalid input, marks can not be more than 100")


# Program1: write a python to create calculator
# user has to three inputs
# input1 : decision 1 = addition, 2 = multiplication 3 = subtraction 4 = divide
# input2 = num1
# input2 = num2
"""
if input1 == 1:
    print(input2 + input3)
elif other condition
"""

# Program2 : three are given you have to identify which nnumber is greater
# a, b, c
# a > b and a >c: print(a)
# b > a and b > c : print(b)
# c > a and c > b : print(c)

# program3 : write program to check that given number is divide by 3 and 5: