"""
result = lambda x, y: x+y

print(result(60, 70))

# Map, Filter, reduce

def get_fact(n):
    fact =1
    for i in range(n, 0, -1):
        fact = fact*i
    return fact

list1 = [5, 7, 2, 8, 3]
result = list(map(get_fact,  list1))

print(result)

square = list(map(lambda x: x**2, list1))
print(square)

# get all even number with filter

even_value = list(filter(lambda x: x%2==0, list1))
print(even_value)

# reduce
from functools import reduce

output = reduce(lambda x, y: x+y, list1)
print("addition :", output)
"""

# Generator

def print_msg():
    return "Good Morning"
    return "Hello How are you"

output = print_msg()
print(output)

def gen_print_msg():
    yield "Hello How are you?"
    yield  "Very good morning"
    yield  "Hope you are doing good"

gen_data = gen_print_msg()
print(gen_data)
print(next(gen_data))
print(next(gen_data))
print(next(gen_data))



def get_square_of_all_number(list1):
    for data in list1:
        yield data**2


list1 = [5, 2, 7, 12, 9]
gen_obj = get_square_of_all_number(list1)
#print(gen_obj)

for i in gen_obj:
    print(i)