#remove : Remove specific data from the list
#
# lists = [6, 4, 3, 16, 12]
# lists.remove(3)
# print("lists:", lists)  # [6, 4, 16, 12]

# pop method : pop method remove data from list using index value, default index value is -1 and
# it also return the removed data.




lists = [6, 4, 3, 16, 12]

# pop with default index -1
var1 = lists.pop()
print(var1)
print(lists)

# pop with specific index 2
var2 = lists.pop(2)
print(var2)
print(lists)




# Program : Write python program to move data from one list to another

list1 = [5, 7, 82, 8, 9]
list2 = []

for i in range(len(list1)):
    var1 = list1.pop(0)
    list2.append(var1)

print("list1:", list1)
print("list2:", list2)





# Write a python program move data from list to dict
list1 = [5, 7, 82, 8, 9]
# output1 = {5: 25,7: 49 , 82:.... } list1 = []
# output2 = [9, 8, 82, 7, 5] , list1 = []

# delete all the data from list
############### Clear method #####################
list11 = [5, 7, 82, 8, 9]

list11.clear()

print(list11)




#### Delete entire list ###
"""
# This will delete entire list from the memory, once it is deleted we can not use it.
list22 = [5, 7, 82, 8, 9]
del list22
print(list22)
"""


###########################################
# Count : get count of any element in the list
list22 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
output = list22.count(8)
print("output 8:", output)




# Program : get count each data in the list and avoid repeatation.
list22 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
# output =
"""
5 : 1
7 : 2
82: 1
8 : 2
9 : 1
2 : 1
12 : 1
"""




################## Get index any element in the list ##########
"""
list33 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
# get index of 82

output = list33.index(82)
print("output 82:", output)

output2 = list33.index(9)
print("output 9:", output2)

"""


############## Sorting of the data ##############

list44 = [5, 7, 82, 8, 9, 7, 2, 8, 12]

# sort method: sort method, sort all the data in the list in acending order by default and modify the list inplace

#list44.sort() # Ascending order
#print("list44: ", list44)

#list44.sort(reverse=True) # Decending order
#print("list44: ", list44)




#__________________________________________
"""
# sorted method : this method sort any sequaltial data type as per
# requirements and it does not modify the list in place.

list55 = [5, 7, 82, 8, 9, 7, 2, 8, 12]

#output55 = sorted(list55) # Ascending order
output55 = sorted(list55, reverse=True)  # Descending order
print("output55:", output55)

print("list55:", list55)

"""



################### Copy data from one list to another #############
# Shallow Copy: when we assign one list to another list and modify second list
# then the changes will reflect on both list

lista = [5, 7, 2, 8, 34]
listb = lista
listc = listb
listb.append(60)
listc.append(70)

print("lista:", lista)
print("listb:", listb)
print("listc:", listc)




# Deep copy : when we copy one list to another list and modify second list
# then the changes will not reflect on first list

listp = [5, 7, 2, 8, 34]
listq = listp.copy()
listq.append(100)

print("listp:", listp)
print("listq:", listq)


################ Reverse the list #############

"""
1. Reverse method
2. Reversed method
3. Slicing
4. For Loop  # class work
5. While Loop  # class work
"""
print("_"*50)
# 1. Reverse method
"""
listp = [5, 7, 2, 8, 34]
listp.reverse()
print("listp:", listp)
"""

"""

# 2. Reversed method:
listp = [5, 7, 2, 8, 34]
listq = reversed(listp)

print("listp:", listp)
print("listq:", listq)
for var in listq:
    print(var, end=" ")


#3: slicing:
listx = [5, 7, 2, 8, 34]
output = listx[::1]  # [34, 2, 5]  #[first index:last index: jump value]
# ::-1 :  it state that default initial index will be -1 and end value will end of the list(positive, negative),
# with -1 jump index.
print(output)

"""

################# List Comprehension ###########

list1 = [5, 7, 8, 2, 9, 2]
#output = [(5, 'odd'), (7, 'odd'), (8, 'even'), (2, 'even'), (9, 'odd'), (2, 'even')]

output = []
for val in list1:
    if val%2 == 0:
        output.append((val, 'even'))
    else:
        output.append((val, 'odd'))
print(output)

# [x for x in list1]


list1 = [5, 7, 8, 2, 9, 2]

# square of all the numbers
result1 = [x**2 for x in list1]
print(result1)

# Get all the even numbers with condition
result2 = [x for x in list1 if x%2 == 0]
print(result2)

# get all the even and odd numbers with if-else condition
result3 = [(x, 'even') if x%2 == 0 else (x, 'odd') for x in list1]
print(result3)

# write python program to check which number is divide by 7
list1 = [5, 7, 21, 49, 22]

# Write a python program to repeat the number three times if it is divide by three else 2 times
list11 = [5, 7, 21, 49, 22]


