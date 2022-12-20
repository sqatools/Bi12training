"""
-> dict contains data in the key value format
-> dict contains only unique key, duplicate keys are not allowed.
-> any type of data can part of value int, float, string, list, tuple, dict
-> only immutable data type can be keys in the dict , int, float, string, tuple
-> Dict does not follow any indexing
"""
dict1 = {'a': 123, 'b': 456}
print(dict1['a'], type(dict1))
dict1['c'] = 789
print(dict1)

"""
school = {
    '10th' : [
        {'std_id': 123, 'name': 'rahul'},
        {'std_id': 456, 'name': 'ankit'},
    ],
    '11th' : [
        {'std_id': 4566, 'name': 'vaibhav'},
        {'std_id': 45623, 'name': 'gourav'},
    ],
    'teachers' : {
        'physics' : [
            {'name': 'phteach1', 'teach_id': 78990},
            {'name': 'phteach2', 'teach_id': 567889}
        ],
    'maths' : [
                {'name': 'mteach1', 'teach_id': 56546},
                {'name': 'mateach2', 'teach_id': 55676}
            ]
    }

}

# Get match teach2 id

print(school['teachers']['maths'][1]['teach_id'])
"""

# duplicate keys are not allowed, if we set duplicate then latest defined value will be considered.
dict1 = {'a': 123, 'b': 456, 'b': 7456}

print(dict1)  # {'a': 123, 'b': 7456}
dict1['a'] = 67898
print(dict1)  # {'a': 67898, 'b': 7456}

# add string to the dict as value
dict1[(5, 7, 8)] = "Good Morning"

# add set as value in the dict
dict1[5.5] = {5, 7, 82, 9}
print(dict1)

# Boolean value as keys
dict1[True] = (4, 6, 7, 8)
print(dict1)

# add list as a key in the dict # TypeError: unhashable type: 'list'
#dict1[[4, 7, 8]] = "Python"
#print(dict1)

# Dictionary methods.
print(dir(dict))
#  'clear', 'copy', 'fromkeys', 'get', 'items',
#  'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# update : update data from one dictionary to another.
"""
dict1 = {'a':" 456", 'b': 234}
dict2 = {'c': 888, 'd': 1234}
dict1.update(dict2)
print("dict1 :", dict1)
print("dict2 :", dict2)



# Get method : Get data from dictionary using key as parameters.
dict1 = {'a':" 456", 'b': 234}
output = dict1.get('a')
print("output :", output)
"""
# pop data dictionary:
dict1 = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
output = dict1.pop('d')
print("pop output :", output)
print("dict1:", dict1)

# popitems : this method removes the data from dictionary and return as key,
# value in tuple format.
"""
dict11 = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
output11 = dict11.popitem()
print(output11)
"""





"""
dict11 = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
dict22 = {}
for i in range(len(dict11)):
    var = dict11.popitem()
    print(var, dict11, dict22)
    dict22[var[0]] = var[1]
print("dict11 :", dict11)
print("dict22 :", dict22)
"""

# items : this method returns list of tuple which has key and value tuple member.
"""
dicta = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
print(dicta.items())
for key, value in dicta.items():
    print("Key:", key, "value:", value)
    
    
    
    
"""
"""
dictb = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
dictb1 = dictb.copy()
dictc = {}

for key, value in dictb1.items():
    var = dictb.pop(key)
    dictc[key] = var

print("dictc:", dictc)
print("dictb:", dictb)
"""


# Clear : Clear all the data from dictionary
dictx = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
dictx.clear()

print("dictx :", dictx)

# Remove entire dictionary from memory
"""
dicty = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
del dicty
print(dicty)  # NameError: name 'dicty' is not defined. Did you mean: 'dict1'?
"""
# keys() : get list of keys in the dictionary
# value() : get list of values in the dictionary
dicty = {'a':456, 'b': 234, 'c': 678, 'd': 63453453}
keys_list = dicty.keys()
values_list = dicty.values()
print(keys_list, values_list)

# Program

"""
for key, value in dit1.items()
    print(key, value)

"""
input_dict = {"a" : "Python", "b": "Programming", "c": "Learning"}
output = {"_a_": "nythonP", "_b_" : "grogramminP", "_c_": "gearninL"}