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

"""

# Add data to the dict
# dict[key] = value

# Update : dict1.update(dict2)

# Remove data from dictionary

# pop method : we have to provide key to get value and remove it

# pop items : remove entire key value pair and return

# get method

# keys : list of keys

# values : list of values

# clear : clear all data from the dict

# del : delete entire variable

# Deep copy and shallow copy in the dictionary

# Shallow copy
dict1 = {'a': 456, 'b' : 234}
dict2 = dict1
dict2['c'] = 555

print("dict1 :", dict1)
print("dict2 :", dict2)

# Deep Copy

dicta = {'a': 456, 'b' : 234, 'p': 567}
dictb = dicta.copy()

dictb['q'] = 678
print("_"*50)
print("dicta :", dicta)
print("dictb :", dictb)


# Move data from one dict to another dictionary
"""
dicta = {'a': 456, 'b' : 234, 'p': 567}
dictb = dicta.copy()
output = {}

print("_"*50)
for key in dictb:
    print(key)
    dict_data = dicta.pop(key)
    print(dict_data)
    output[key] = dict_data

print("_"*50)
print("dicta :", dicta)
print("dictb :", dictb)
print("output :", output)

"""
########################################
# Write a python program to get bill on the basis of user purchase

fruit_stock = {'apple': 20, 'banana' : 25, 'mango': 50}
fruit_price = {'apple': 50, 'banana' : 10, 'mango': 100}
fruit_purchase = {'apple': 5, 'banana' : 10, 'mango': 6}

"""
-> apply loop on fruit_purchase dict and get fruit name quatity "for fruit, qua  in fruit_purchase.items()"
-> Get each fruit_bill = fruit_qua * fruit price : "qua*fruit_price[fruit]"
-> add each fruit bill in total amount : "total_amount = total_amount + fruit_bill"
-> update fruit_stock dict data with reduce each fruit quantity  : fruit_stock[fruit] = fruit_stock[fruit] - qua
-> add each fruit bill in output_dict
"""

Output_bill_amount = {}
total_amount = 0

for fruit, qua in fruit_purchase.items():
    fruit_bill = fruit_price[fruit]*qua
    total_amount = total_amount + fruit_bill
    fruit_stock[fruit] = fruit_stock[fruit] - qua
    Output_bill_amount[fruit] = fruit_bill

print("_"*50)
print("Total Amount :", total_amount)
print("Each Fruit Bill :", Output_bill_amount)
print("Remainig Stock:", fruit_stock)

print("_"*50)
for fruit, bill in Output_bill_amount.items():
    print(fruit ,":", fruit_purchase[fruit], ":", fruit_price[fruit],":", bill)

print("Total Bill :",  total_amount)

# Write a python program to provide salary oncrement to the employee on the basis of number yr experience
"""
if exp > 10 : 20% increment
if exp >= 5 and exp < 10 : 10% increment
if exp < 5  then : 5% increment

"""
employee = [
    {'name': 'Vrunda', 'email': 'vrunda@gmail.com', 'experince' : '5yr', 'salary': 500000},
    {'name': 'Amit', 'email': 'Amit@gmail.com', 'experince' : '7yr', 'salary': 600000},
    {'name': 'Amar', 'email': 'Amar@gmail.com', 'experince' : '8yr', 'salary': 700000},
    {'name': 'Janardhan', 'email': 'Janardhan@gmail.com', 'experince' : '10yr', 'salary': 1000000},
    {'name': 'Vishal', 'email': 'Vishal@gmail.com', 'experince' : '4yr', 'salary': 400000},
]


#1 Write a python program to get the output
# if age > 25 then change marital status as M else 'UM'

#dict1 = {'name' : ['Rahul', 'Mahesh', 'Gourav'], 'Age' : [56, 26, 20], 'kids': [3, 1, 0], 'emp_status': ['Yes', 'No', 'No']}

#ouptut = {'name' : [('Rahul', 'M'), ('Mahesh', 'M'), ('Gourav', 'UM')], 'Age' : [56, 26, 20], 'kids': [3, 1, 0], 'emp_status': ['Yes', 'No', 'No']}

#2 Write a python program to get the output

#str2 = "Saidly today India lost Semifinal"

#output = {'Saidly': 'Saidly', 'today': 'today', 'India' : 'India', 'lost': 'Won', 'Semifinal': 'Semifinal'}

"""
dict1 = {'Age' : [21, 56, 20, 56, 78, 23], 'name' : ['Rahul', 'Mahesh', 'Gourav', 'kiran', 'sahil', 'pramod'],  'kids': [3, 1, 0], 'emp_status': ['Yes', 'No', 'No']}

output = {}
name_list = []
# Loop through each key and value
for key, value in dict1.items():
    # check if given key is equal to 'Age'
    if key == 'Age':
        # If given key is 'Age' then loop through all list of value of the 'Age'
        # using range loop
        for i in range(len(dict1[key])):
            # Now check each age value is greater than 25 or not
            if dict1[key][i] > 25:
                # if age value is greater than 25 then set user name as Married in tuple format
                name_data = (dict1['name'][i], 'M')
                name_list.append(name_data)
            else:
                # if age value is greater than 25 then set user name as UnMarried in tuple format
                name_data = (dict1['name'][i], 'UM')
                name_list.append(name_data)
                
        # Add name and age key values in the output dict.
        output['name'] = name_list
        output[key]  = value
    elif key == 'name':
        continue
    else:
        output[key] = value

print("Output:", output)
"""

"""
if exp > 10 : 20% increment
if exp >= 5 and exp < 10 : 10% increment
if exp < 5  then : 5% increment

"""

employees = [
    {'name': 'Vrunda', 'email': 'vrunda@gmail.com', 'experience' : '5yr', 'salary': 500000},
    {'name': 'Amit', 'email': 'Amit@gmail.com', 'experience' : '7yr', 'salary': 600000},
    {'name': 'Amar', 'email': 'Amar@gmail.com', 'experience' : '8yr', 'salary': 700000},
    {'name': 'Janardhan', 'email': 'Janardhan@gmail.com', 'experience' : '10yr', 'salary': 1000000},
    {'name': 'Vishal', 'email': 'Vishal@gmail.com', 'experience' : '4yr', 'salary': 400000},
]

output_list = []

"""
step 1:  Apply loop on the employee list "for emp in employee"
step 2:  Apply loop with key value in specific employee dict    "for kye,value in emp.items()"
step 3:  Check key if it is equal to experience    "if key == 'experience'"
step 4:  If above condition in true then get experience value in int form    exp_value = int(value[0])
step 5:  Now check exp_value coming in which range with elif condition  
        if exp_value > 10, elif exp_value > 5 and exp_value < 10 elif exp_value <= 5
        
step6: if exp_value > 10 is True provide salary increment with 20%
          emp['salary'] = emp['salary'] + emp['salary']*(20/100)
          
step7: if exp_value > 5 and exp_value < 10 is True provide salary increment with 10%
          emp['salary'] = emp['salary'] + emp['salary']*(10/100)
          
step8: if exp_value < 5 and exp_value < 10 is True provide salary increment with 5%
          emp['salary'] = emp['salary'] + emp['salary']*(5/100)

"""

#step 1:  Apply loop on the employee list "for emp in employee"
for emp in employees:
    emp_copy = emp.copy()
    # step 2:  Apply loop with key value in specific employee dict    "for kye,value in emp.items()"
    for key, value in emp_copy.items():
        #step 3:  Check key if it is equal to experience    "if key == 'experience'"
        if key == 'experience':
            # step 4:  If above condition in true then get experience value in int form    exp_value = int(value[0])
            exp_value = int(value[0])
            # step 5:  Now check exp_value coming in which range with elif condition
            #         if exp_value > 10, elif exp_value > 5 and exp_value < 10 elif exp_value <= 5
            if exp_value >= 10:
                # step6: if exp_value > 10 is True provide salary increment with 20%
                #           emp['salary'] = emp['salary'] + emp['salary']*(20/100)
                emp_copy['salary'] = emp_copy['salary'] + emp_copy['salary'] * 20/100

            elif  exp_value > 5 and exp_value < 10:
                # step7: if exp_value > 5 and exp_value < 10 is True provide salary increment with 10%
                # emp['salary'] = emp['salary'] + emp['salary']*(10/100)
                emp_copy['salary'] = emp_copy['salary'] + emp_copy['salary'] * 10 / 100
            elif  exp_value <= 5:
                # step8: if exp_value < 5 and exp_value < 10 is True provide salary increment with 5%
                #        emp['salary'] = emp['salary'] + emp['salary']*(5/100)
                emp_copy['salary'] = emp_copy['salary'] + emp_copy['salary'] * 5 / 100
            else:
                continue



    print(emp_copy)
    output_list.append(emp_copy)



print(employees)

print(output_list)