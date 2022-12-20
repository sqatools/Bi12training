class employee:
    """
    -> add employee details
        empid_1={"name":"john", "email": "john@gmail.com"}
    -> update the employee data with id
    -> delete employee data
    -> get employee specific details of any employee
    """
    def __init__(self, databasefile = 'employee.txt'):
        self.databasefile = databasefile

    def add_employee_details(self, **kwargs):
        with open(self.databasefile, 'r') as file:
            file_lines = file.readlines()
            print(file_lines)
            if file_lines == ['\n']:
                new_emp_id = f"empid_1"
            else:
                last_emp_details = file_lines[-1]
                last_emp_id = int(last_emp_details.split("=")[0].split("_")[1])
                new_emp_id = f"empid_{last_emp_id+1}"


        new_emp_data = f"{new_emp_id}={kwargs}\n"
        with open(self.databasefile, 'a') as file:
            file.write(new_emp_data)



if __name__== '__main__':
    obj = employee()
    obj.add_employee_details(name='amit1', email='amit1@gmail.com', phone=64565666546, salary=70000)


