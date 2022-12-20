Set1 = {5, 7, 8, 9, 2, 4, 1, 5, 7}

print(Set1, type(Set1))

"""
-> Set is mutable data type, we add modify the data in set.
-> Set is unstructure data type it does not follow any indexing
-> Set only contains unique values, duplicate data is not allowed.
-> We can add any type of data in the set except list and dictionary
"""
seta = {5, 7, 8, 'a', 'b'}
# Methods in the set
print(dir(seta))
"""
'add', 'clear', 'copy', 'difference', 
'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 
'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']
"""

# add content to the set
input_tuple = (6, 2, 8, 1, 5)
seta.add(input_tuple)
print(seta)

#add list to the set
"""
list1 = [5, 7, 2, 7]
seta.add(list1)
print(seta)
"""
# TypeError: unhashable type: 'list'

# Add dict to the set
"""
dict1 = {'a': 456, 'b': 234}
seta.add(dict1)
"""
# TypeError: unhashable type: 'dict'

seta.add('Python')
seta.add(2.5)

print("seta:", seta)

# write a python program to add data from list to set
"""
list1 = [5, 7, 2.6, 'Python', (3, 6, 2), [5, 6], {'a': 345, 'b': 123}]
output_set = {5, 7, 2.6, (3, 6, 2), 'Python'}

var = [5, 7]
dict1 = {123:'a', 456: 'b'}
print(isinstance(var, dict))
"""

setx = {6, 8, 2, 9, 10}
sety = {1, 4, 2, 6, 3}

#output = setx + sety # This is not possible
#print(output)

# Update data from one to set to another
"""
setx.update(sety)
print("setx :", setx)
print("sety :", sety)

# Remove data from set
# remove method : we can specify any element from set to remove.
setx = {6, 8, 2, 9, 10}
setx.remove(9)
print("setx after removing 9:", setx)

# pop method :  this method remove any random value from set and return it
setx12 = {6, 8, 'a', 2, 9, 'b', 10, 15, 23}
pop_output = setx12.pop()
print(pop_output)


# Python Program to copy content from set to another with its square and if it is string then repeat it two times.
set1 = {6, 2, 7, 1, 'b', 8, 23, 14, 'a'}
output = {'square of all the poped values'}

# Clear all the content from the set
# Clear method : clear all the data from the set.

seth = {6, 2, 7, 1, 'b', 8, 23, 14, 'a'}
seth.clear()
print("seth :", seth)

# copy method :

# Shallow copy concept
setp = {6, 2, 7, 1, 'b', 8, 23, 14, 'a'}
setq = setp
setq.add("Programming")

print("setp: ", setp)
print("setq :", setq)

# deep copy concept
print("__"*50)
setr = {6, 2, 7, 1, 'b', 8, 23, 14, 'a'}
setv = setr.copy()

setv.add("Language")
print("setr:", setr)
print("setv:", setv)


# Union : Union of 2 sets:  Combine all the unique values from both the sets and return output
print("__"*50)
set11 = {5, 7, 2, 8, 3}
set22 = {6, 18, 2, 19, 7}

output = set11.union(set22)
print(output)
print("set11:", set11)
print("set22:", set22)
output.add(66)
print("Union output:", output)

# Difference
set33 = {5, 7, 2, 8, 3}
set44 = {6, 18, 2, 19, 7, 2, 8}

diff_output1 = set33.difference(set44)
diff_output2 = set44.difference(set33)
print("diff_output :", diff_output1) # {3, 5}
print("diff_output :", diff_output2) # {18, 19, 6}

#output = set()
"""


set33 = {5, 17, 12, 8}
set22 = {7, 2, 8}
set44 = {6, 18, 2, 19, 7, 2, 8}

print("Subset :",set33.issubset(set44))  # False
print("Subset :",set22.issubset(set44))  # True

# check super set
print("super set :", set44.issuperset(set22)) # True
print("Super Set :", set44.issuperset(set33)) # False

# intersection : this  means what are common in two sets
setx = {7, 2, 8, 10}
sety = {6, 18, 2, 19, 7, 2, 8}
print(set44.intersection(set22))


# Write a python program to find out common values between two list
# list1 = [5, 7, 2, 8, 1]
# list2 = [3, 6, 2, 7, 1, 9]
# output = [7, 2, 1]

# Symmetric Different between two set, it means all the uncommon values in both the sets.
setp = {7, 2, 8, 10}
setq = {6, 18, 2, 19, 7, 2, 8}
print(setq.symmetric_difference(setp))

# Program : Find out all the uncommon values between two tuples.
tup1 = (5, 7, 2, 8, 1)
tup2 = (1, 7, 12, 56, 8)
output = (5,  12, 56, 2)

# Program : Find out all the uncommon values between two dict values
# dict1 = {'a' : [4, 7, 8, 2, 8], 'b': [3, 6, 1, 8], 'c': [2, 5, 1, 7, 9]}
# dict2 = {'a' : [14, 17, 8, 2, 18], 'b': [13, 6, 1, 88], 'e': [2, 5, 1, 7, 9]}
# output_dict = {'a' : [14, 17, 4, 7], 'b': [3, 13, 88]}

# Program 4 : Write a python program to calculate factorial of all prime number
list1= [1, 2, 4, 6, 7, 14, 13]
output4 = [(1, 1), (2, 2), (7, 'factorial value'), (13, 'factorial value')]
# fact 5 : 5*4*3*2*1

# Program 5 : Write a python manupulate the string
# re-arrange the string where odd index words will come first and even index words will come last.
input = "Hey very good Morning"
Output = "very Morning Hey Good"




dict1 = {'a' : [4, 7, 8, 2, 8], 'b': [3, 6, 1, 8], 'c': [2, 5, 1, 7, 9]}
dict2 = {'a' : [14, 17, 8, 2, 18], 'b': [13, 6, 1, 88], 'e': [2, 5, 1, 7, 9]}
#output_dict = {'a' : [14, 17, 4, 7], 'b': [3, 13, 88]}

output_dict = {}
# Loop in dict1 to get its key value
for key, value in dict1.items():
    temp = []
    # Check key of dict1 is available in dict2
    if key in dict2:
        # apply loop on each values of dict1 key
        for data in value:
            # check dict1 key data is available in dict2 key data
            if data in dict2[key]:
                continue
            else:
                temp.append(data)
        for data2 in dict2[key]:
            if data2 in value:
                continue
            else:
                temp.append(data2)

        output_dict[key] = temp
    else:
        continue

print(output_dict)