num1 = 10
print(type(num1))

print(id(num1))


# 1: Assign values to multiple variables

a, b, c = 60, 50, 70
print(a, b, c)

# 2 : Assign same value to multiple variables
p = q = r = 100
print(p, q, r)

# 3 compare multiple variables values
x = 40
y = 50
z = 60
print(x == y == z)  # False

x1 = y1 = z1 = 600
print(x1 == y1 == z1)  # True

# Operation with variable data
"""
There are some operator through we cab perform operation
+ : Plus
- : Minus
* : Multiplication
/ : Divide : it gives result in decimal
// : it gives result in int
%  : Remainder operator
= : Assignment operator
== : equal to operator
** : Power operator
"""

# Plus two numbers
num1 = 40
num2 = 50
add_output = num1 + num2
print("addition :", add_output)

# Subtraction of two numbers
num11 = 100
num22 = 50
sub_out = num11 - num22
print("subtraction :", sub_out)

# Multiplication of two numbers
a = 4
b = 20
mul_out = a*b
print("Multiplication :", mul_out)

# Division single / and double //

num1 = 13
output = num1/2  #single slace /
print(output, type(output))


output2 = num1//2 # double slace //
print("output2:", output2, type(output2))


# Remainder operator %
x = 11
rem_output = x%2
print("rem_output:", rem_output)

y = 10
rem_output2= y%2
print(rem_output2 == 0) # Even
z = 15
rem_output3= z%2
print(rem_output3 == 0) # Odd

# Get square of any numbers with power operator **

num11 = 4

sqr = num11**2
print("square of 4:", sqr)
print("Cube of any number :", 5**3)


# Get output od given equation
# x + y + 2xy(x-y) + x2 + y2
x = 5
y = 6
output = x + y + 2*x*y*(x-y) + x**2 + y**2
#        5 + 6 + 2*5*6*(5-6) + 25 + 36
#        11 + 60*-1 + 61
#        11 - 60 + 61
print(output)  # 12


# Home Work
"""
a2 – b2 = (a – b)(a + b)
(a + b)2 = a2 + 2ab + b2
a2 + b2 = (a + b)2 – 2ab
(a – b)2 = a2 – 2ab + b2
(a + b + c)2 = a2 + b2 + c2 + 2ab + 2bc + 2ca
(a – b – c)2 = a2 + b2 + c2 – 2ab + 2bc – 2ca
(a + b)3 = a3 + 3a2b + 3ab2 + b3 ; (a + b)3 = a3 + b3 + 3ab(a + b)
(a – b)3 = a3 – 3a2b + 3ab2 – b3 = a3 – b3 – 3ab(a – b)
a3 – b3 = (a – b)(a2 + ab + b2)
a3 + b3 = (a + b)(a2 – ab + b2)
(a + b)4 = a4 + 4a3b + 6a2b2 + 4ab3 + b4
(a – b)4 = a4 – 4a3b + 6a2b2 – 4ab3 + b4
a4 – b4 = (a – b)(a + b)(a2 + b2)
a5 – b5 = (a – b)(a4 + a3b + a2b2 + ab3 + b4)

"""






















