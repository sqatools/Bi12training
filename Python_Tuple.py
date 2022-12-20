#Tuple
"""
-> Tuple is immutable datatype, once it is defined we can not change the data.
-> Any type of data can be part of tuple
-> Tuple follows same positive and negative indexing similar like string and list
"""

tup1 = (4, 7, 8, [4, 7, 3], (2, 4, 5),
        {'a': 123, 'b': 567}, 'Programming')

print(tup1, type(tup1))

# Positive Indexing
output = tup1[3]
print(output[2]) # 3





# Negative indexing
output2 = tup1[-2]
print(output2) # {'a': 123, 'b': 567}
print(output2['a'])

# Slicing in the tuple

result = tup1[2:6]
print("result:", result)  # (8, [4, 7, 3], (2, 4, 5), {'a': 123, 'b': 567})


result2 = tup1[:-3]
print("result2:", result2)  # (4, 7, 8, [4, 7, 3])





#######################

tup11 = (4, 7, 8, [4, 7, 3], (2, 4, 5),
        {'a': 123, 'b': 567}, 'Programming')

#loop without indexing
for val in tup11:
        print(val)

print("_"*50)
#loop with indexing
for i in range(len(tup11)):
        print(tup11[i])






# Check any give data is available in the tuple or not
tup22 = (4, 7, 8, [4, 7, 3], (2, 4, 5),
        {'a': 123, 'b': 567}, 8, 'Programming', 4, 8)

val = 16
output22 =True if  val in tup22 else False
print("output22 :", output22)

# Methods is the tuple
print("_"*50)
print(dir(tuple))



# 'count', 'index'
# Get count 4
print("_"*50)
output4 = tup22.count(4)
print("output4:", output4)  #2

output5 = tup22.count(8)
print("output5:", output5)  #3





# Program to get of all the data and avoid dupliation.

tup33 = (4, 7, 8, [4, 7, 3], (2, 4, 5),
        {'a': 123, 'b': 567}, 8, 'Programming', 4, 8)

list1 = []
print("_"*50)
for val in tup33:
        if val in list1:
                continue
        else:
                print(val,":", tup33.count(val))
                list1.append(val)


# Index method : get index position of any given element
print("_"*50)
tup33 = (4, 7, 8, [4, 7, 3], (2, 4, 5),
        {'a': 123, 'b': 567}, 8, 'Programming', 4, 8)

print("index of 7:", tup33.index(7)) #1
print("index of (2, 4, 5):", tup33.index((2, 4, 5))) #4

###############################
#Modify data in the tuple
print("_"*50)

tuple12 = (5, 7, 8, 9)

list1 = list(tuple12)
list1.append(12)
print(tuple(list1))
print("tuple12:", tuple12)



# Modify data in tuple in place
print("_"*50)
list2 = [6, 7, 8]
tuple13 = (5, 11, list2, 44, 9) # (5, 11, [6, 7, 8], 44, 9)
print(tuple13)

list2.append(23)
print(tuple13)  # (5, 11, [6, 7, 8, 23], 44, 9)

#######################################################
# reverse the tuple
tupa = (6, 2, 7, 8, 9)
print("_"*50)
# Reverse with slicing
output = tupa[::-1]
print(output)

# Reverse with reverse method
print("_"*50)

output2 = reversed(tupa)
print("output2", output2)
for data in output2:
        print(data, end=" ")

# Reverse with Loop
print()
print("_"*50)
tupb = (6, 2, 7, 8, 9)
for i in range(-1, -len(tupb)-1, -1):
        print(tupb[i], end=" ")


######################### Sorted method to sort the tuple ##########
print()
print("_"*50)
tupc = (6, 2, 7, 8, 9)
print(tuple(sorted(tupc))) # (2, 6, 7, 8, 9)


############## Find out sum, max and mini numbers in the tuple ###########
# Program to get sum of all the numbers
tupc = (6, 2, 7, 8, 9)
tup_sum = 0

for val in tupc:
        tup_sum = tup_sum + val
print("sum of all the values :", tup_sum)
print("sum of all the values with in built method :", sum(tupc))

list11 = [6, 8, 3, 8, 2, 6, 8, 9]
print("sum of list values:", sum(list11))

# Program to get max values from tuple
print("_"*50)
tuple11 = (16, 8, 3, 18, 22, 66, 8, 9)

max_num = 0
for data in tuple11:
        print("max value:", max_num, "data:", data)
        if data > max_num:
                max_num = data
        else:
                continue

print("max value in the tuple:", max_num)
print("get max value from tuple using in built method:", max(tuple11))

# Write a python to get minimum number from tuple with logic
print("get mini value from tuple using in built method:", min(tuple11))

# Programs 1 : Find the second largest number from the tuple

# Programs 2 : Python program to find all the prime numbers in tuple
# Prime number : the number which are divide it self or 1.

# Program 3: Python program to check all the palindrome numbers in tuple
# tuple = (5, 7, 8, 23, 131, 243, 545, 787)
# output = (131, 545, 787)

# Program 4: Write a python program to find out the largest prime in the tuple
#input = (5, 7, 8, 12, 21, 61, 97, 101, 78)  # 101

print("_"*50)
tuple11 = (16, 8, 3, 18, 22, 66, 8, 9)

#max_num = 0
# for data in tuple11:
#         print("max value:", max_num, "data:", data)
#         if data > max_num:
#                 max_num = data
#         else:
#                 continue
#
max_num = 0
output = [data if data > max_num else max_num for data in tuple11]
print(output)

