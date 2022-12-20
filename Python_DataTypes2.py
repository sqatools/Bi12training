# list
"""
list1 = []   # empty list
list2 = list() # empty list

print(list1, list2, type(list1), type(list2))  #[] [] <class 'list'> <class 'list'>
list3 = [4, 2.5, 'hello', 'h', (5, 7, 8), [4, 2, 8]]

# [4, 2.5, 'hello', 'h', (5, 7, 8), [4, 2, 8]] <class 'list'>
list4 = [
    "Python",
    "Programming",
    [4, 7, 2],
    (6, 8, 3)
]

# ['Python', 'Programming', [4, 7, 2], (6, 8, 3)] <class 'list'>
print("list3 :", list3, type(list3))
print("list4 :", list4, type(list4))
"""

#        0      1        2              3          4
lista = [124, 'Python', 'Programming', [4, 7, 2], (6, 8, 3)]
#       -5      -4       -3            -2          -1


output = lista[2]
print(output, type(output))

print(output[2])  # o

print(lista[2][3]) # g

output2 = lista[-2]
print(output2, output2[1]) # [4, 7, 2] 7

print(lista[-2][1])


"""
Properties :

-> list is mutable data, once data is defined we can modify at any point of time
-> list can contains any type of data as list member. int. float, string, list, tuple, dict, boolean
-> List follows same indexing as like string (positive and negative indexing)
"""
"""
#Length of list
print(len(lista))  # 5

str2 = "Good Morning"
print(len(str2))  # 12

listb = [5, 3, 6, 8, 2, 9]

outputb = listb[2: 5]
print("outputb :", outputb)

outputc = listb[: 5]  # [6, 8, 2]
print("outputb :", outputc) # [5, 3, 6, 8, 2]
outputd = listb[3: ]
print("outputd :", outputd)  #[8, 2, 9]

listb.append(70)
print(listb)   # [5, 3, 6, 8, 2, 9, 70]

listb.append([6, 8, 3])  # [5, 3, 6, 8, 2, 9, 70, [6, 8, 3]]
print(listb)

listb.extend([3, 5, 6])  # [5, 3, 6, 8, 2, 9, 70, [6, 8, 3], 3, 5, 6]
print(listb)

list3 = [5, 7, 3] + [6, 2, 8]  # [5, 7, 3, 6, 2, 8]
print(list3)

listb.remove([6, 8, 3])
print(listb)
"""

###################### Tuple #####################
"""
tup1 = ()  # Empty Tuple
tup2 = tuple()  # Empty Tuple

print(tup1, tup2, type(tup1), type(tup2))  # () () <class 'tuple'> <class 'tuple'>
#         0  1   2    3       4      5                     6         7
tuplea = (5, 6, 2.5, 'Hello', 'G', [6, 7, 8, "Python"], (6, 3, 8), {'a': 1, 'b': 2})
#         -8 -7 -6    -5      -4     -3                    -2         -1

print(tuplea, type(tuplea))
outputa = tuplea[5]
print(outputa)  # [6, 7, 8, 'Python']
outputc = tuplea[5][3][1]
print(outputc)  # y

# Get negative index
outputd = tuplea[-1]
print(outputd, type(outputd))

print(tuplea[1: 6])  # (6, 2.5, 'Hello', 'G', [6, 7, 8, 'Python'])

tup2 = (5, 6, 7)
"""
"""
Properties :

-> tuple is immutable data, once data is defined we can not modifythe data
-> tuple can contains any type of data as list member. int. float, string, list, tuple, dict, boolean
-> tuple follows same indexing as like string (positive and negative indexing)
"""

############################## Dictionary ###########################
# Dict can data in key value format
# dict1 = {key: value}

dict1 = {}
dict2 = dict()
print(dict1, dict2, type(dict1), type(dict2))

"""
Properties :
-> dict store data in key value format
-> dict is a mutable data type, once data is defined as modify at any point of time
-> dict is an un-structure data type, which does not follow any indexing.
-> dict does not allow to add duplicate key
-> We can add any type of data as value in the dictionary
-> We can add only immutable data type can key in the dictionary.
"""

dict1 = {'name': 'Kiran', 'salary': 50000, 'job': 'Data Analyst'}
print(dict1, type(dict1))

dict1['email'] = 'kiran@gmail.com'
print(dict1, type(dict1))  # {'name': 'Kiran', 'salary': 50000, 'job': 'Data Analyst', 'email': 'kiran@gmail.com'}
print(dict1['name']) # Kiran

# check duplicate key is allowed or not
dict1['name'] = 'Amar'
print(dict1, type(dict1))

# add different data as value
dict1['a'] = 2
dict1[(5, 7, 2)] = 2.5
dict1[33] = 'Python'
dict1[50.55] = [5, 7, 3]
dict1['f'] = (7, 8, 9)
dict1['new_dict'] = {'address': 'Mumbai', 'country': 'India'}

print(dict1)

#dict1[[5, 7, 8]] = 60  # TypeError: unhashable type: 'list'
#print(dict1)

#


"""
school = {
    'teacher' : {
        'physics' : [
            {'name': 'phy01', 'email': 'phy0@gmail.com', 'address': 'mumbai', 'phone': 345667},
            {'name': 'phy02', 'email': 'phy2@gmail.com', 'address': 'Pune', 'phone': 3456654357},
            {'name': 'phy03', 'email': 'phy3@gmail.com', 'address': 'Bang', 'phone': 88345667},
            {'name': 'phy04', 'email': 'phy4@gmail.com', 'address': 'Hyder', 'phone': 99345667}
        ],
        'math' : [
            {'name': 'math01', 'email': 'math0@gmail.com', 'address': 'mumbai', 'phone': 5345667},
            {'name': 'math02', 'email': 'math2@gmail.com', 'address': 'Pune', 'phone': 35456654357},
            {'name': 'math03', 'email': 'math3@gmail.com', 'address': 'Bang', 'phone': 848345667},
            {'name': 'math04', 'email': 'math4@gmail.com', 'address': 'Hyder', 'phone': 299345667}
        ],
        'chemestry' : [],
        'lab assistant' : [],
        'science' : []
    },
    'student' : {
        '10th' : [
            {'name': 'stu10_1', 'email': 'stu10_1@gmail.com', 'phone': 45667 },
            {'name': 'stu10_2', 'email': 'stu10_2@gmail.com', 'phone': 456675454 }
        ],
        '11th' : [
            {'name': 'stu11_1', 'email': 'stu11_1@gmail.com', 'phone': 4775667 },
            {'name': 'stu11_2', 'email': 'stu11_2@gmail.com', 'phone': 45776675454 }
        ],
        '12th' : [
            {'name': 'stu12_1', 'email': 'stu12_1@gmail.com', 'phone': 45552667 },
            {'name': 'stu12_2', 'email': 'stu12_2@gmail.com', 'phone': 4562675454 }
        ]
    },
    'other_staff' : {
        'account' : [],
        'security' : [],
        'swiper' : []

    }
}
print(school['teacher']['physics'][3]['phone'])
"""


#################### Set data type ############

"""
-> Set is mutable data type, we can modify it
-> Set is structure data type, does not follow any indexing
-> set contain only unique data, duplicate data is not allowed.
-> we can add any type of data in the set except and dict, list

"""

set1 = set()
set2 = {5, 7, 'c', 8, 2, 8, 5, 1, 'a', 'b'}

print(set2, type(set2))

##########################  Boolean (True, False) ############
a = 10
b = 20
c = 10
print(a == b)  # False
print(a == c)  # True

# False : When expected condition is not matching
# True : When expected condition is matching