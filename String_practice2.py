"""
Str :
->  String is immutable data type, once it is defined we can not changed.
->  String is follows indexing (positive and negative) to read the content.
->  Any char or word or statement can be considered as string.
"""
str1 = "Python"
print(str1,  type(str1))

name = "Swapnil"
age = 23
salary = 100000
# Hello my name is Swapnil and my age is 23, I earn 100000  rupees per month
# String Formating

# Plus operator
result1 =  "Hello my name is "+name+" and my age is " + str(age) +" I earn " +str(salary)+ " rupees per month"
print(result1)

# Format method
result2 =  "Hello my name is {} and my age is {} I earn {} rupees per month".format(name, age, salary)
print(result2)

# F string formating

result3 =  f"Hello my name is {name} and my age is {age} I earn {salary} rupees per month"
print(result3)

# Indexing :  String follows both positive and negative index
# (left to ritgh -> positive indexing : default initial index 0
# right to left -> negative indexing  : default initial index -1
#Exmaple
"""
 0 1 2 3 4
 H E L L O
-5-4-3-2-1
"""
str2 = "Programming"
# 3 index char
print(str2[3])  # g

# -4 index char
print(str2[-4])  # m
# Slicing : We get a substring with the help slicing rules.

# Rule1 : str[initial index : end index] : In this rule, we will get substring
# from initial index to end_index -1 value

str11 = "Learning"
output11 = str11[2:5]
print("output11 :", output11 ) # arn

# Rule2 : str[: end_index] : in this rule default initial index will be zero.
# and substring will get from zero to end_index-1

str22 = "Learning"
output11 = str11[:5]
print("output11 :", output11 ) # Learn


# Rule3 : str[initial_index: ] : in this rule default end_index will be total len of the string.
# and substring will get from initial_index to end of the string

str33 = "Learning"
output22 = str11[2:]
print("output22 :", output22 ) # arning

# Rule4: str[initial_index:end_index:jump_index] : In this rule will get substring  from initial index to end_index-1
# with jump of index values.

str44 = "Learning"
output44 = str44[1:6:1]
print("output44 :", output44 ) # earni

str44 = "Very Good Morning"
output55 = str44[2:10:2]
print("output55 :", output55) # r od

stra = "Very Good Morning"
outputa = stra[-1:-10:-1]
print("outputa :", outputa) # gninroM d

outputb = stra[1:-8:-1]
print("outputb :", outputb) # No output

outputb = stra[-1:8:-1]
print("outputb :", outputb) # gninroM

# Rule5 : str[initial_index :: jump_index] : In this rule default end_index will be len of the string.

strc = "Very Good Morning"
outputc = stra[1::2]
print("outputa :", outputc) #eyGo onn

strc1 = "Very Good Morning"
outputc1 = strc1[-1::-1]
print("outputa :", outputc1)  # gninroM dooG yreV
# Rule6 str[::jum_index]
# for positive jump index default initial index will be 0 and end index will be end of the string
# for negative jump index default initial index will be -1 and end_index will be -end_index
"""
strc11 = "Very Good Morning"
outputc11 = strc11[::-1]
print("outputa :", outputc11)  # gninroM dooG yreV
strc22 = "Very Good Morning"
outputc22 = strc22[::1]
print("outputa :", outputc22)  # Very Good Morning
outputc23 = strc22[::2]
print("output23 :", outputc23)  # Vr odMrig


# Program : Find out the every second element from the string.
str1 = "Programming"
output = str1[1::2]
print(output)   # rgamn

# Program : Find out the first and last two character of the given string
str1 = "Programming"
#output = Prng
var1 = str1[:2]
var2 = str1[-2:]
#print(var1, var2, var1+var2) # Prng

# Program : Write a python program to swap first character of the string
str1 = "Programming"
#output = "grogramminP"
first = str1[0]
last = str1[-1]
middle = str1[1:-1]
#print(last+middle+first)

# apply loop on the string
str1 = "Very Good Morning"
for char in str1:
    #print(char)

print("_"*30)
print("length :", len(str1))
for i in range(len(str1)):
    #print(str1[i])
"""

# String Methods.
print(dir(str))
"""
'capitalize', 'casefold', 'center',
 'count', 'encode', 'endswith', 
 'expandtabs', 'find', 'format', 
 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 
 'isdigit', 'isidentifier', 'islower', 
 'isnumeric', 'isprintable', 'isspace', 
 'istitle', 'isupper', 'join', 'ljust', 
 'lower', 'lstrip', 'maketrans', 
 'partition', 'removeprefix', 
 'removesuffix', 'replace', 
 'rfind', 'rindex', 'rjust', 
 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
 'startswith', 'strip', 'swapcase', 
 'title', 'translate', 'upper', 'zfill'
"""

# count method : this methods help to get count of each character in the given string.

# # Get count of all the characters
# for char in str1:
#     print(char,":", str1.count(char))

# program : get count of unique characters.
"""
str1 = "Very good morning, We are learning Python"
temp = ""
for char in str1:
    if char in temp:
        continue
    else:
        print(char, ":", str1.count(char))
        temp = temp + char
    print("temp :", temp)
"""

# index: get index of any character in the given string
str1 = "Very good morning, We are learning Python"
# If we have repeated characters then it will return index of first character occurance
print(str1.index('g'))  # 5
print(str1.index('We'))  # 19

for i in range(len(str1)):
    print(str1[i], ":", i)
# upper(), lower(),  isUpper(), isLower()
str1 = "Very Good MorNing, We ArE leAGrning Python"
print(str1.upper())  # VERY GOOD MORNING, WE ARE LEGRNING PYTHON
print(str1.lower()) # very good morning, we are leagrning python
str11 = "PYTHON"
str22 = "programming"
print(str11.isupper()) # True
print(str22.isupper()) # False

print(str11.islower()) # False
print(str22.islower()) # True


# Program : write a python program to covert all even index char into upper char and odd index char into lower case
str1 = "Very Good MorNing, We ArE leAGrning Python"
output = ""

for i in range(len(str1)):
    if i%2 == 0:
        output = output + str1[i].upper()
    else:
        output = output + str1[i].lower()
print(str1)
print(output)

# Split() Method, this method help to split any string with given delimeters and
# return as list of words/substring

str1 = "Very Good MrNing, We AorE leAGrning Python"
output1 = str1.split(" ")
print(output1) # ['Very', 'Good', 'MorNing,', 'We', 'ArE', 'leAGrning', 'Python']

str2 = "Very_Good_MorNing_We_ArE_leAGrning_Python"
output2 = str2.split("_")
print(output2)  # ['Very', 'Good', 'MorNing', 'We', 'ArE', 'leAGrning', 'Python']

output3 = str1.split("o")
print(output3) # ['Very G', '', 'd M', 'rNing, We ArE leAGrning Pyth', 'n']






url = "https://www.google.co.in"
#server = "google.co.in"
#protocol = "https"
#w = "www"

output = url.split("//")
print(output)
"""
protocol = output[0][:-1]
print(protocol)

w = output[1][:3]
print("word wibe web:", w)

server = output[1][4:]
print("server name:", server)
"""
"""
protocol = url.split("//")[0][:-1]
print("Protocol :", protocol)
w = url.split("//")[1][:3]
print("w:", w)
server = url.split("//")[1][4:]


url = "https://www-google.co.in"
server2 = url.split("//")[1].split("-")[1]
print(server2)
"""

#Replace Method : this method help to replace word1 with word2
"""
str1 = "We are learning Programming and its Fun"
output = str1.replace("Programming", "Cricket")
print(output)
print(output.replace("learning", "practicing"))

print(str1.replace("Programming", "Cricket").replace("learning", "practicing"))
print(str1.replace("Programming", "Cricket").replace("learning", "practicing").replace('a', 'b').split(" "))
"""

# Write a python program to replace specific char
input_Str = "Learning Prodfdfgramming is fun and easy to learn"
#  get wordlist with split()
word_list = input_Str.split(" ")
output = ""
temp = ""
"""
-> get wordlist with split()
-> go through each word using loop for word in word_list
-> Check word is equal to required word
-> Get index of 'g' char from the word.
-> apply loop using word leg and range:
-> Match each index with g char index
-> once it is match then replace it with special char temp = temp + "$"
-> else add all other char with no change.
-> then add temp into output string
-> 

"""
"""
#  go through each word using loop for word in word_list
for word in word_list:
    # Check word is equal to required word "Progamming"
    if word == 'Prodfdfgramming':
        # Get index of 'g' char from the word.
        char_index = word.index('g')
        #  apply loop using word leg and range:
        for i in range(len(word)):
            # Match each index with g char index
            if i == char_index:
                # once it is match then replace it with special char temp = temp + "$"
                temp = temp + "$"
            else:
                # else add all other char with no change.
                temp = temp + word[i]

        output = output + temp

    else:

        output = output + word + " "

print("Output :", output)
"""



# Reverse the string
"""
1. slicing
2. loop
3. while loop
4. reversed method.
"""
# 1. slicing
str1 = "Python"

print(str1[::-1])

# 2 loop
for i in range(-1, -len(str1)-1, -1):
    print(str1[i], end="")

# 3 while loop
print("\n")
num = -1
temp = ""
while num > -len(str1)-1:
    temp = temp + str1[num]
    num = num -1

print(temp)

# 4. reversed method.
str2 = "Programming"
output = reversed(str2)
print(output)
for char in output:
    print(char, end="")






