list1 = [4, 7, 2, 8, 3, 2, 8]
#print(list(set(list1)))

# Program to remove all the duplicates from the list.

"""
output = []
for var in list1:
    if var in output:
        continue
    else:
        output.append(var)


print(output)
"""
"""
def remove_duplacte():
    code
"""

def remove_duplicte(list1):
    output = []
    for var in list1:
        if var in output:
            continue
        else:
            output.append(var)
    print(output)


#list2 = [5, 7, 2, 8, 2, 4, 5, 7, 2]
#list3 = [5, 17, 2, 18, 2, 4, 15, 17, 12, 15]
#remove_duplicte(list2)
#remove_duplicte(list3)

def addition(num1, num2):
    print("addition :", num1+num2)


# global variable
vara = 50

def function1():
    varb = 60 # local variable
    print(vara+varb)

def function2():
    varc = 70 # local variable
    print(vara+varc)

function1()
function2()