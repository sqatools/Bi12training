class employee:
    # Class variables
    city = 'Mumbai'
    _address = 'Boravali Street'
    __country = 'India'

    # Instance method
    def __init__(self, name, company, salary):
        # Instance Variable
        self.name = name
        self._company = company
        self.__salary = salary

    # Instance method
    def show_emp_name(self):
        print("Employee name :", self.name)

    # Instance method
    def _show_company(self):
        print(f"Employee working in company: {self._company}")

    # Instance method
    def __show_salary(self):
        print(f"employee salary is : {self.__salary}")


    # Class Method
    @classmethod
    def show_empolyee_general(cls):
        print("city:", cls.city)
        print("Address :", cls._address)
        print("country:", cls.__country)
        #print("Name :", cls.name) we can not access instance variable in the class method
        #cls.show_emp_name() # we can not access instance method in the class method

    @staticmethod
    def static_method_get_factorial(num):
        fact =1
        for i in range(num, 0, -1):
            fact = fact*i

        return fact


if __name__ == '__main__':
    #obj = employee('Rahul', 'Facebook', '50lac')
    #obj.show_empolyee_general()
    #print(obj.static_method_get_factorial(5))
    output = employee.static_method_get_factorial(6)
    print(output)


