"""
-> List is mutable datatype, we can modify
-> List follows positive and negative
-> We can add anytype of data and list member , int, float, list, tuple, dict, set, Boolean
-> While defining no need to mention its size

"""
#        0  1   2    3
list1 = [4, 6, 2.4, 'Python', [5, 7, 8], (2, 5, 8), {'a': 123, 'b': 478}]
#        -4 -3 -2   -1


output = list1[2]
print(output, type(output))
output1 = list1[-1]
print(output1)


sub_list = list1[4]
print(sub_list)
print(sub_list[1])
print(list1[4][1])

print(list1[-1]['a'])

# List Methods

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

#print(dir(list))

lista = [5, 7, 8, 2]

# Add data to the list

# -> Append : add data at end of the list
print("_"*50)
lista.append(50)
print("lista:", lista)

# Insert method
print("_"*50)
lista.insert(2, 100)
print(lista)

# Extend Method : add all the data from one to another
print("_"*50)
listc = [1, 6, 34, 11]
listb = [4, 7, 3, 8]

#listc.extend(listb)
#print("listc:", listc)

listc.insert(-10, 300)
print("listc:", listc)

listc.insert(10, 400)
print("listc:", listc)

#print(listc[6])

listc[-1] = 500

print(listc)

listd = [5, 8, 2, 9]

listd[0] = 10
print(listd)

listd.insert(0, 20)
print(listd)

# add two list with plus operator
output1 = listb + listc
print(output1)

############## Remove data from the list ##########
# Remove : remove data from list with value
listx = [5, 8, 3, 9]
listx.remove(9)
print(listx)

# pop : remove data from list with index and return it
listy = [3, 6, 2, 8, 1, 5]
output = listy.pop() # by default index will be -1
print(output)
print(listy)

output2 = listy.pop(1)
print(output2)
print(listy)

# Clear method
listy.clear()
print(listy)

# Del : delete data from memory
del listy
#print(listy)

# copy data from one list to another
# Shallow Copy
print("_"*30)
list11= [5, 7, 2, 8]
list22 = list11
list22.append(20)

print("list11:", list11)
print("list22:", list22)

print(id(list11), id(list22))


# Deep Copy
print("_"*30)
list33 = [5, 7, 8, 11]
list44 = list33.copy()
list44.append(99)

print(list44)
print(list33)
print(id(list33), id(list44))

#############################
# sort list data : sort method
print("_"*30)
list1 = [4, 6, 2, 8, 1, 9]
list1.sort(reverse=True)

print("list1:", list1)

# Sorted method
list2 = [5, 7, 2, 8, 1, 3]

output = sorted(list2)
print(output)
print("list2:", list2)

# Reverse the list
# reverse method

print("_"*30)
# case1 : reverse method
list2 = [5, 7, 2, 8, 1, 3]
list2.reverse()
print("list2:", list2)

#Case2 : Reversed method

print("_"*30)
list3 = [5, 7, 2, 8, 1, 3, 6, 2]
output = reversed(list3)
print(output)
for data in output:
    print(data, end=" ")


print()
#set1 = {3, 'a', 7, 3, 5, 61, 8, 5, 'Python', (4, 7, 2), {'a': 345, 'b': 4567}}

#print(set1)


import pandas as pd
from collections import OrderedDict

dict1  = { 'b': [567, 6, 7, 6], 'c': [5, 2, 7, 8], 'a': [5, 23, 7, 11], 'd': [2, 5, 1, 5]}

output = dict(sorted(dict1.items()))

print(output)

output2 = dict(sorted(dict1.items(), key=lambda item: item[0]))

print(output2)

