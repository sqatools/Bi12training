"""
Polymorphism : when a single entity perform multiple task is known polymorphism

-> Method overriding : When we have inheritance between two class and both class have same
  method name, then child class method will get preference when its object is being created.
  parent class method will be overwritten by child class method.

-> Method Overloading : When one class have two method with same name difference functionality
  , then it is known as method overloading, but python does not support this feature.
  if we defined two method with same name, then it will consider latest defined method.


-> Operator Overloading
"""

class company:
    def __init__(self, company_name):
        self.company = company_name

    def welcome_msg(self):
        print("Welcome to the Company")

    def show_company(self):
        print("We are in company class")
        print("company name:", self.company)


class employee(company):
    def __init__(self, name, designation, salary, company):
        super().__init__(company)
        self.name = name
        self.designation = designation
        self.salary = salary


    def show_employee_details(self):
        print(f" Employee Name : {self.name} \n"
              f" Employee Designation :{self.designation} \n"
              f" Employee Salary : {self.salary}")

    # this method will not consider to execute
    def show_company_working_hour(self):
        print("Total 8 hr/day employee has to work")


    def show_company_working_hour(self, hour):
        print(f"Total {hour} hr/day employee has to work")

    def show_company(self):
        print("We are in employee class")
        print("company name:", self.company)
        self.show_employee_details()



if __name__ == '__main__':
    obj = employee('Shivam', 'Data Analyst', '20Lac', 'DataMatics')
    #obj.show_company()
    obj.show_company_working_hour(10)



# Operator Overloading
num1 = 50
num2 = 60

print(num1 + num2)

print(num1.__add__(num2))
str1 = 'Hello'
str2 = 'Morning'

print(str1 + str2)

print(str1.__add__(str2))

