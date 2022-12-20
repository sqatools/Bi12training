"""
Single underscore as prefix '_'
  -> If we declare any variable or method with single '_' then it does not visible in the
   suggestion list
  -> If we want to access var/method with single underscore we can access it directly with
    the obj   obj.var/method

Double underscore as prefix '__'
    -> If we declare any variable or method with double underscore ( '__')  then it does not visible in the
   suggestion list
    -> If we want to access var/method with double underscore( __ ) prefix, then we have
        follow a pattern which is obj._classname__var/method
"""
class employee:
    # Class variables
    city = 'Mumbai'
    _address = 'Boravali Street'
    __country = 'India'

    def __init__(self, name, company, salary):
        # Instance Variable
        self.name = name
        self._company = company
        self.__salary = salary

    # Instance method
    def show_emp_name(self):
        print("Employee name :", self.name)

    def _show_company(self):
        print(f"Employee working in company: {self._company}")

    def __show_salary(self):
        print(f"employee salary is : {self.__salary}")


if __name__ == '__main__':
    obj = employee('Kiran', 'Facebook', '50Lac')
    print(obj._address)
    obj._show_company()
    print(obj._company)

    ########## access class member with double under _classname__var/method

    print(obj._employee__country)
    obj._employee__show_salary()

    print(dir(obj))


