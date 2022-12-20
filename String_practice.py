"""
capitalize', 'casefold', 'center',
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

# Strip : this method remove the ending and training spaces
"""
str1 ="  Python Programming  "
print(str1)
output = str1.strip()
print(output)

# lstrip and rstrip

output2 = str1.rstrip()
print(output2)

output3 = str1.lstrip()
print(output3)
"""
# Find method : This method return the index of substring and return -1 if it is not available.
"""
str11 = "dfdsjjkl;jasdfasfdaf  learning afdaf  dfadf word  python"
output = str11.find("learning")  # 22
print(output)

output = str11.find("LLearning")  # -1
print(output)
"""

# Join Method
str22 = "Morning"

output = "_".join(str22)
print(output)

# Program : Write a python program to print desired output
str1 = "Tomorrow onwards we will enjoy world cup 2022"
#  replace all the vowel with special characters
# output1  =  "T$m$rr$w $nw$rds w$ will $njoy w$rld c$p 2022"

# join odd length word with - and even with *
# output2 = "T-o-m-o-r-r-o-w o*n*w*a*r*d*s w-e w*i*l*l e*n*j*o*y w*o*r*l*d c*u*p 2-0-2-2"

# join odd length word first and last char repeat 2 time - and even length word first and last char repeat 2 time
# ouptu3 = "TTomorroww ooonwardsss wwweeee wwwillll eenjoyy wworldd ccupcc 22202222"


# Tiletle : Method method convert first char of each into camel case.
str11 = "Tomorrow onwards we will enjoy world cup 2022"

output = str11.title()
print(output) # Tomorrow Onwards We Will Enjoy World Cup 2022


# Swapcase:
"""
str11 = "TomOrrow onWards wE will enJoy wOrld cUp 2022"
output22 = str11.swapcase()

print(output22)  # tOMoRROW ONwARDS We WILL ENjOY WoRLD CuP 2022

# chr : this takes ASCII values as input and provide alphates

print(chr(90))

# 65-90 : A-Z
# 97-123 : a-z

for i in range(65, 91):
    print(chr(i), end=" ")

print("\n")
for i in range(97, 123):
    print(chr(i), end=" ")
"""

stra = "TomWorrow onWards WE Will enJoy world cUp 2022"

outputa =  stra.split('O')
print(outputa)

# isnumeric
"""
str11 = "2345"

print(str11.isnumeric())   #True
print(str11.isdigit())     # True

str22 = "345Hello"
str33 = "Hello"

print("str22 :", str22.isalnum())   # True
print("str33 :", str33.isalnum())   # True

print("str22 :", str22.isalpha())    # False
print("str33 :", str33.isalpha())    # True



"""
"""
Interview Questions
1. Can we modify the string : We can not modify the string because its immutable
2. slicing : 
     -> find first two and last two char
     -> reverse the string with slicing
     -> get all odd char
     -> get all even char   
   
3. Replace : 
     -> Replace one with another word
     -> replace multiple words at a time.
     
4. Split:
     -> Remove all duplicate words from the string
     -> Get max word from the string
     -> get count of each character in the string
     -> replace vowels with some special character
     
5. lower(), upper(), islower(), isUpper(), swapcase()
6. join method : python : p-y-t-h-o-n
7. isnumeric : get all the mobile numbers from the given string.
8. get all the email id from given string.
9. 



     
"""

name = "Kiran Darade"
output = " ".join(name.split()[::-1])
print(output)