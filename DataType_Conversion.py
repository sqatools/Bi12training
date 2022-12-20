#### Int  ###

num1 = 40
# int -> float : possible
output = float(num1)
print(output, type(output))

# int -> string : possible
num11 = 123
output = str(num11)
print(output, type(output))

print(output[1]) # 2


# int ->  list # not possible
"""
num2 = 456
output = list(num2)
print(output)  # TypeError: 'int' object is not iterable
"""

# int -> tuple # not possible
"""
num2 = 456
output = tuple(num2)
print(output)  # TypeError: 'int' object is not iterable
"""
# int -> dict # not possible
"""
num2 = 456
output = dict(num2)
print(output)  # TypeError: 'int' object is not iterable
"""

# int -> set # not possible
"""
num2 = 567
output = set(num2)
print(output)  # TypeError: 'int' object is not iterable
"""
# int = boolean

# num1 = 0 # False
# num1 = 123  # True
"""
output = True if num1 else False
print(output)
"""


################# Float ###########
var1 =45.80

# float -> int # possible

output = int(var1)
print(output,  type(output))

# float -> string  # possible
output = str(var1)
print(output,  type(output))

print(output[-1])  #8

# float -> list : not possible
# float -> tuple : not possible
# float -> dict : not possible
# float -> set : not possible
# Float -> Boolean
# if any float variable has data then it will return True else False


############### String ###################

str1 = "Hello"

# str1 -> int # This conversion is possible when string
# only contains numbers.
"""
output = int(str1) # invalid literal for int() with base 10: 'Hello'
print(output)
"""
"""
str2 = '4578'
output2 = int(str2)
print(output2, type(output2))
"""

# str -> float # This conversion is possible when string
# only contains decimal values or numbers
"""
str1 ="Python"
output = float(str1)  # ValueError: could not convert string to float: 'Python'
print(output)
"""
"""
str2 = "45.67"
output1 = float(str2)
print(output1, type(output1))
"""


### string -> list # possible
"""
str1 = "Programming"
output = list(str1)
print(output, type(output))  # ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
"""
### string -> tuple # possible
"""
str1 = "Programming"
output = tuple(str1)
print(output, type(output)) # ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')
"""


######### string -> dict # this conversion when string
# follows proper dict properties and we can use json for this
# conversion.
"""
str1 = "Tech Focus"
output = dict(str1)  # dictionary update sequence element #0 has length 1; 2 is required
print(output)

"""
"""
import json

str22 = '{"name": "rahul", "age": 25, "address": "Pune"}'
print(str22, type(str22))

jsonn_output = json.loads(str22)
print(jsonn_output, type(jsonn_output))

print(jsonn_output['age'])

jsonn_output['email'] = 'rahul@gmail.com'
print(jsonn_output)

"""


###### string - set # possible

str1 = "Programming"
output = set(str1)
print(output, type(output))  # {'a', 'g', 'm', 'P', 'i', 'r', 'n', 'o'} <class 'set'>


# Str -> Boolean

str1 = ""
str2 = "Hello"
output = True if str1 else False
print(output) # False
output2 = True if str2 else False
print(output2) # True

############# List ##########

# list -> int : not possible
# list -> flaot : not possible
# list -> string # possible

list1 = [5, 7, 2, 8]
output = str(list1)
print(output, type(output))
print(output[0], output[2])

# list -> tuple : possible
list2 = [5, 7, 8]
output = tuple(list2)
print(output,  type(output)) # (5, 7, 8) <class 'tuple'>

"""
# list -> dict : not possible
list3 = [4, 6, 8]
output = dict(list3)
print(output)  # TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""

# list -> set : possible

list3 = [4, 6, 8, 5, 4, 1]
output = set(list3)
print(output) # {1, 4, 5, 6, 8}

# list -> boolean
"""
list1 =[]
list2 = [5, 7]

output1 = True if list1 else False
print(output1)

output2 = True if list2 else False
print(output2)
"""
########## Tuple ##########

# tuple -> int : not possible
# tuple -> float : not possible
# tuple -> string : possible
tup1 = (5, 7, 3)
output = str(tup1)
print(output, type(output), output[-1])

# tuple -> list : possible
tup1 = (5, 7, 3)
output = list(tup1)
print(output, type(output), output[-1])

# tuple -> dict : not possible
# tuple -> set
tup1 = (5, 2, 6, 1, 1, 2, 5)
output = set(tup1)
print(output, type(output))

# tuple -> Boolean

tup1 = ()
tup2 = (5, 7)
output1 = True if tup1 else False
print(output1) # False

output2 = True if tup2 else False
print(output2) # True

############### Dictionary ##############

# dict -> int : not possible
# dict -> float : not possible
# dict -> string : possible

dict1 = {'a': 345, 'b': 567}
output = str(dict1)
print(output, type(output), ":", output[0], ":", output[2])

# dict -> list : possible , it return list of keys of the dict.
dict1 = {'a': 345, 'b': 567}
output = list(dict1)

print(output)  # ['a', 'b']

# dict -> tuple : possible
dict1 = {'a': 345, 'b': 567}
output = tuple(dict1)

print(output)  # ('a', 'b')

# dict -> set # possible it returns set of keys
dict1 = {'a': 345, 'b': 567}
output = set(dict1)
print(output, type(output)) # {'b', 'a'} <class 'set'>

# dict -> Boolean
dict1= {}
dict2 = {'a': 123, 'b': 456}

output = True if dict1 else False
output2 = True if dict2 else False
print(output)
print(output2)


####### Set  ######
# set -> int # not possible
"""
set1 = {5, 7, 8}
output = int(set1)
print(output)
"""
# set -> float : not possible
# set -> string # possible
set1 = {5, 'a', 6, 7, 2}
output = str(set1)
print(output,  type(output), output[4])
# set -> list : possible
set1 = {5, 7, 8, 2, 5, 7}
output = list(set1)
print(output, type(output), output[0])

# set -> tuple : possible
set1 = {5, 7, 8, 2, 5, 7}
output = tuple(set1)
print(output, type(output), output[0])
# set -> dict # not possible
"""
set1 = {5, 7, 8, 2, 5, 7}
output = dict(set1)
print(output, type(output), output[0])
"""
# set -> Boolean
set1 = {}
set2 = {5, 6}
output = True if set1 else False
output2 = True if set2 else False
print(output, output2)