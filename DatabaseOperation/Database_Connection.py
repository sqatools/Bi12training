import sqlite3
from faker import Faker

con = sqlite3.connect('school.db')
fk = Faker()

#crate_table_query = "create table student(name char, phone char, email char)"
#con.execute(crate_table_query)


#data_query = "insert into student(name, phone, email) values('Rahul', 6543645364, 'rahul@gmail.com')"
#con.execute(data_query)
# con.commit()

#select_query = "select * from student"
#data = con.execute(select_query)
#print(data)

#for val in data:
#    print(val)


# insert bulk data to the data base

for i in range(1, 101):
    first_name = fk.first_name()
    user_phone = fk.phone_number()
    user_email = fk.email()
    data_query = f"insert into student(name, phone, email) values('{first_name}', '{user_phone}', '{user_email}')"
    print(data_query)
    con.execute(data_query)
    con.commit()
con.close()
