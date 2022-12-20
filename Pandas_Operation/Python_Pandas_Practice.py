"""
Series
DataFrame

Command to install pandas on the machine
"""

import pandas as pd

"""
list1 = [43, 6, 2, 'x', 'y', 'z']

sr = pd.Series(list1)

print(sr)

print(sr[0])
print("_"*40)
sr2 = pd.Series(list1, index=['a', 'b','c', 'd', 'e', 'f'])

print(sr2)

print(sr2['e'])
print(sr2[1])
print("_"*40)
list2 = [5, 6, 7, 2, 8, [4, 2, 5]]
sr3 = pd.Series(list2)

print(sr3*2)

# Create series with dictionary
print("_"*40)
dict1 = {'name': ['Rahul', 'mohit', 'akash'], 'age': [19, 23, 24], 'salary': [70000, 50000, 30000]}

sr3 = pd.Series(dict1)
print(sr3)

print(sr3['name'])

# Create series with tuple
print("_"*40)
Tupl1 = (5, 7, 2, 8)

sr4 = pd.Series(Tupl1)

print(sr4)

"""
# create a series with set which is not allowed
"""
print("_"*40)
set1 = {5, 4, 7, 1, 7,  2}
sr5 = pd.Series(set1)
print(sr5)
"""
"""
Error
Traceback (most recent call last):
  File "E:\Trainings\PythonTraining3Oct22_Bi12\Pandas_Operation\Python_Pandas_Practice.py", line 51, in <module>
    sr5 = pd.Series(set1)
          ^^^^^^^^^^^^^^^
  File "E:\Trainings\PythonTraining3Oct22_Bi12\venv\Lib\site-packages\pandas\core\series.py", line 470, in __init__
    data = sanitize_array(data, index, dtype, copy)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Trainings\PythonTraining3Oct22_Bi12\venv\Lib\site-packages\pandas\core\construction.py", line 611, in sanitize_array
    raise TypeError(f"'{type(data).__name__}' type is unordered")
TypeError: 'set' type is unordered

"""
"""
# Get unique data from the series
print("_"*40)
list1 = [5, 6, 2, 5, 1, 5]

sr = pd.Series(list1)
print(sr)
#pd.unique(sr)

print(sr.unique())
"""
############################################ Data Frame ##############

"""
print("_"*40)
dict1 = {
    'name' : ['Amit', 'Sanket', 'Yogesh', 'Mohit'],
     'age' : [20, 23, 21, None],
     'address' : ['Pune', 'Mumbai', 'Kolkata', 'Bangalore']
}


df = pd.DataFrame(dict1, index=['a', 'b', 'c', 'd'])
print(df)


print(df['age'][0])

df['salary'] = [50000, 30000, 54000, 70000]

print(df)


# Delete any specific colomn from the data frame
del df['age']
print("_"*40)
print(df)

# update any specific data in the data frame
print("_"*40)
df['salary']['b'] = 80000

print(df)

per_name = 'amit'

for data in df.iterrows():
    print(data)
    #print(data[1]['name'], data[1]['address'], data[1]['salary'],)
    #print("_"*40)

    if data[1]['name'] == 'Amit':
        print(data[1]['salary'])



"""
#############################################
"""
# Sum of two column

dict1 = {'Bill' : [400, 700, 5000], 'grocery' : [6000, 8000, 7000]}

df = pd.DataFrame(dict1, index=['Jan', 'Feb', 'March'])

df['total'] = df['Bill'] + df['grocery']

print(df)
"""


# Get unique data from the series
"""
print("_"*40)
list1 = [5, 6, 2, 5, 1, 5]

sr = pd.Series(list1)
print(sr)
#pd.unique(sr)

print(sr.unique())
"""

student1 = {'name': ['Rahul', 'gourav', 'amit', 'mahesh'],
           'age' : [20, 21, 23, 25],
           'city' : ['Mumbai', 'Pune', 'Bangalore', 'Hyderabad']}

student2 = {'name': ['keshav', 'vishal', 'pandit', 'sharma'],
           'age' : [30, 32, 33, 35],
           'city' : ['Chennai', 'Delhi', 'Gurgaov', 'Indore']}
df1 = pd.DataFrame(student1)
df2 = pd.DataFrame(student2)
#print(df1)
#print(df2)
output = df1.append(df2, ignore_index=True)
print(output)

# Convert data frame data CSV format
# csv_data = output.to_csv()
# print("_"*40)
# print(csv_data)

# with open('student_data.csv', 'a') as file:
#     file.write(csv_data)
#

# loc function to apply filter
data = output.loc[2, 'age']
print(data)  #23

# Get details with city name
print("_"*50)
data2 = output.loc[(output.city == 'Mumbai') | (output.name == 'amit')]
print(data2)

print("_"*50)
# Get all whose age greater than 30
data3 = output.loc[(output.age >= 30)]
print(data3)


# # Get data from sql
# print("_"*50)
# data4 = output.to_sql('userdata', 'con')
# print(data4)

# Get data on the basis of index
print("_"*50)
data5 = output.iloc[0:5]
print(data5)


print("_"*50)
data6 = output.iloc[5:8]
print(data6)


# Read exel data with Pandas
#import openpyxl
"""
we should install openpy excel on the machine
pip install openpyxl
"""
excel_data = pd.read_excel('test_data.xlsx', sheet_name='Sheet2')
print(excel_data)
