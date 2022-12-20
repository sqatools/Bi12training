"""
Python data type

i : Numbers
   1) Integer
   2) Float
   3) Imaginary

ii : Sequence
   1) String
   2) List
   3) Tuple

iii : Dictionary
iv : Sets
v : Boolean
"""


######## Integer  <class 'int'> ############
"""
-> Integer is a immutable data type, once it is defined, we can not change it.
-> Integer data does not have any limitation, we can assign any long data to variable.
"""
"""
var1 = 30
print(var1, type(var1))

var2 = 45243526262634563456435
print(var2, type(var2))

# Preview data will be overwritten
var2 = 100
print("var2 :", var2, type(var2))

# if we will add two int value then output will be int

var3 = 60
var4 = 50
output = var3 + var4
print("output :", output, type(output))

# will single slace division the number output will be float
output2 = 11/2
print(output2, type(output2))
"""

######### Float <class 'float'> ############
"""
-> Float is a immutable data type, once it is defined, we can not change it.
-> Float data does not have any limitation, we can assign any long data to variable.
"""

var1 = 2.5
print(var1, type(var1))

var3= 475757656.4645646911
print(var3, type(var3))   # 475757656.4645647 <class 'float'>

num1 = 4.5
num2 = 5.5
output1 = num1 + num2
print("output1: ", output1, type(output1))   # 10.0 <class 'float'>
# Add an int and float

output2 = 30 + 2.5
print("output2 :",output2,  type(output2))

######################## Sequence data type (string) <class 'str'> ################
str1  = "My Tech Focus"

print(str1, type(str1))  # <class 'str'>

str2 = 'Python'
# slace consider string as single line
str3 = 'Python' \
       'Programming'
# slace consider string as single line
str4 = "1. addition" \
       "2. subtraction" \
       "3. multiplication"

str5 = '''Your Blogger blog’s content will be 
downloaded to your computer in an XML file. 
Once the download is complete, it is time to 
import your Blogger content into your WordPress site.'''

str6 = """
Your Blogger blog’s content will be downloaded to 
your computer in an XML file. Once the download 
is complete, it is time to import your Blogger
content into your WordPress site.
"""
"""
print("_"*50)
print("str1:", type(str1), str1)
print("_"*50)
print("str2:", type(str2), str2)
print("_"*50)
print("str3:", type(str1), str3)
print("_"*50)
print("str4:", type(str4), str4)
print("_"*50)
print("str5:", type(str5), str5)
print("_"*50)
print("str6:", type(str6), str6)

"""

"""
# \n move cursor to next line

str7 = "Hello We are \n\n\n Learning Python"
print(str7)

# \t add space in between words.
print("_"*50)
str8 = "Python is very \t\t easy to learn"
print(str8)

# Convert entire string in the raw format
print("_"*50)
str9 = r"Python is very \t\t easy to \n\n\n\n learn"

print(str9)
"""

# String follows positive and negative index , due to this string is sequencial data type
var1 = "Good"

""" 
0  1  2  3 # positive
G  O  O  D
-4 -3 -2 -1 # Negative
"""
"""
# Positive Index example
output = var1[0]
print("output :", output)

output2 = var1[3]
print("output2 :", output2)

# String Slicing Example
var2 = "Programming"
print(var2[2:6])

# Negative index examples
var3 = "Learning"

output3 = var3[-1]
print("output3 :", output3)

output4 = var3[-3]
print("output4 :", output4)

var2 = "Programming"
print(var2[-7:-2])
"""
"""
str1 = "Python Programming"

print(str1[2:6:1])



list1 = [4, 6, 7, 8]
list1.append(5)
print(list1)

str1 = "Hello" 

str3 = str1 + "Python"

int
list
str
"""

################# List #####################

