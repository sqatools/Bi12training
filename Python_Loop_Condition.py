"""
for i in range(1, 10, 1):
    print(i)
"""

# range(initial value, end value, jump between each value)
# range value iterate till (end value -1)

# range(10)  : default initial value is zero 0, and default difference value is 1
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(2, 10)  : initial value is zero 2, and default difference value is 1
# 2, 3, 4, 5, 6, 7, 8, 9

# range(1, 10, 2) :
# 1, 3, 5 ,7 ,9

# range(10)
for k in range(10):
    print(k)

print("_"*10)
# range(2, 10)
for k in range(2, 10):
    print(k)

print("_"*10)
# range(1, 10, 2)
for k in range(1, 10, 2):
    print(k)

# Program : Write a program to get all even numbers from 1 to 30
# even : number which divide by 2 is even
print("_"*10)
for i in range(1, 30):
    if i%2 == 0:
        print(i)

# Program : write a program to get all the number which are divide by 5 and 7 between 1 to 100.

print("_"*10)
for j in range(1, 100):
    if j%5 == 0 and j%7 == 0:
        print(j)




# Read data from different data type with loop

str1 = "Python"
print("_"*50)
# loop on string data
for char in str1:
    print(char)

# loop on string with indexes
str_len = len(str1)
print(str_len)
print("_"*50)
for i in range(str_len):
    print(i, str1[i])




#### read List data with loop
print("_"*50)
list1 = [5, 7, 2, 5, 8]

for var in list1:
    print(var)

print("_"*50)
#list_len = len(list1)
for i in range(len(list1)):
    print(i, list1[i])

# read dictionary data with loop
print("_"*50)
dict1 = {'a': 345, 'b': 123, 'c': 333}

for val in dict1:
    print(val)
"""
a
b
c
"""

for val in dict1.items():
    print(val)
"""
('a', 345)
('b', 123)
('c', 333)
"""

for key, val in dict1.items():
    print("key :", key,  "val:", val)

"""
key : a val: 345
key : b val: 123
key : c val: 333
"""

# Nested loop Condition
"""
for condition1:
    for condition2:
        code
"""

for add in range(1, 6): # add = 1, 2
    for pkg in range(1, 4): # pkg: 1, 2, 3: 1, 2, 3
        print("add :", add, "pkg:",  pkg)

    print("_"*50)

"""
*
* *
* * *
* * * *
* * * * *
"""
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
"""
"""
* * * * *
* * * *
* * *
* *
*
"""
"""
print("_"*20)
for k in range(6, 0, -1):
    for l in range(k):
        print("*", end=" ")
    print()
"""

"""
# for i in range(10):
#     print(i, end=" ")
print("_"*20)
for i in range(10, 1,):
    print(i)

"""

################### While Loop ###############
"""
while condition:
    code
"""
"""
n = 10
temp = 0

while n >= temp:
    print(temp)
    temp = temp + 1
"""
# write a python to reverse any number
"""
num1 = 123
# output = 321
result = 0
var1 = num1%10
print(var1)

result = var1*10
num1 = num1//10
print(num1)

var1 = num1%10
print(var1)
result = result + var1
print(result)
result = result*10
print(result)


var1 = num1//10
print(var1)
result = result + var1
print("result :",  result)
"""

"""
n = 14354565675
result = 0

while n > 0:
    temp = n%10
    result = result*10 + temp  #
    n = n//10

print("result :", result)
"""
"""
# Infinite True
while True:
    print("Very good morning")
"""
# calculator with while loop

"""
while True:
    dec_input = int(input("Please enter your required:\n"
                          "1. addition\n"
                          "2. multiplication \n"
                          "3. subtraction \n"
                          "4. division\n"))
    if dec_input == 1:
        num1 = int(input("enter first number:"))
        num2 = int(input("enter second number:"))
        print("addition :", num1+num2)
    elif dec_input == 2:
        num1 = int(input("enter first number:"))
        num2 = int(input("enter second number:"))
        print("multiplication :", num1*num2)
    elif dec_input == 3:
        num1 = int(input("enter first number:"))
        num2 = int(input("enter second number:"))
        print("subtraction :", num1-num2)
    elif dec_input == 4:
        num1 = int(input("enter first number:"))
        num2 = int(input("enter second number:"))
        print("division :", num1/num2)
    else:
        print("Invalid Input, value should be between 1 to 4")
        break

    print("__"*50)

"""
####################
"""
for i in range(1, 20):
    if i == 4 or i == 7 or i == 9:
        continue
    print(i)
"""
"""
for i in range(1, 20):
    if i == 4 or i == 7 or i == 9:
        break
    print(i)
"""

# write a python program to check given number is prime or not.
import time
num = 13454556
prime = True
t1 = time.time()
for i in range(2, num//2):
    if num%i == 0:
        prime = False
    else:
        continue
t2 = time.time()

print("Total execution time:",  t2 - t1)

if prime:
    print("This number is prime number :", num)
else:
    print("This is not prime number :", num)