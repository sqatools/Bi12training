#        0  1   2   3       4
list1 = [4, 6, 'a', 2.5, 'Hello']
#       -5  -4  -3  -2    -1
print(list1, type(list1))
"""

var1 = list1[0]
print(var1, type(var1)) #

var2 = list1[-1]
print(var2, type(var2))  # Hello <class 'str'>

list11 = [4, 6, 'a', 2.5, 'Hello',
          [5, 7, 8], (2, 5, 7), {'a': 234, 'b': 678}
          ]




print(list11[5][1])

# Slicing
lista = [6, 8, 2, 9, 24, 67]

# first index with default last next
output = lista[1:]
print(output) # [8, 2, 9, 24, 67]

output1 = lista[2:4]
print(output1) # [2, 9]

#reverse the list
output2 = lista[::-1]
print(output2)


output3 = lista[1::2]
print(output3)
"""
########################## apply loop on the list ###########
"""
print("_"*50)
print()
list1 = [5, 7, 2, 8, 23, 56]

for var in list1:
    print(var, var**2)

# get values with index
list_len = len(list1)
print("_"*50)
print()
for i in range(list_len):
    print(i, list1[i], list1[i]**2)

# Get odd numbers from the list:
print("_"*50)
print()
for var in list1:
    if var%2 != 0:
        print(var)
    else:
        continue

"""


############################### List methods ##############################
print(dir(list))

"""
'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""


listb = [5, 7, 2, 8, 34]
# Add data to the list
# Append : this method add element at the end of the list

listb.append(50)
print(listb)

listb.append('Python')
print(listb)

listb.append([5, 7, 8])
print(listb)

# get data from list to add to the another list
# list1 = [5, 2, 7, 12, 30, 67, 89, 15, ]
# output1 = []
# output2 = [12, 30, 15] # numbers which are divide by 3


# Insert Method : this method help to insert data at the specific position/index.
print("*"*50)
list1 = [5, 2, 7, 12, 30, 67, 89, 15]
list1.insert(2, 'Python')
print(list1)

list1 = [5, 2, 7, 12, 30, 67, 89, 15]
list1.insert(2, (6, 8, 3, 9))

print(list1)

# Extend Method : This method extend data from one list to another.
print("_"*40)
listb = [6, 3, 7, 8]
listc = ['a', 'c', 'd', 'e']

listc.extend(listb)

print(listc)
print(listc[4])

# concatenate 2 list with plus operator

listp = [6, 3, 7, 8]
listq = ['a', 'c', 'd', 'e']

listr = listp + listq
print("listr :", listr)
print("listp :", listp)
print("listq :", listq)

# Remove data from the list

# remove : Remove specific data from the list

lists = [6, 4, 3, 16, 12]
lists.remove(3)
print("lists:", lists)  # [6, 4, 16, 12]


###############
# Insert any element in the list after the target element (with insert method)
# Class Work: Insert any element in the list after the target element (with append method)

input = [6, 4, 3, 16, 12, 15, 23, 45]
var1 = 60
tar = 15
list_len = len(input)

for i in range(list_len):
    if input[i] == tar:
        input.insert(i+1, var1)
        break
    else:
        continue

print("input list:", input)


