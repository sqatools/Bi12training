"""
Inheritance :
#1. Single Inheritance : Class A -> Class B (Father -> Son)
#2. Multi Level Inheritance : Class A -> Class B -> Class C (Grandfather -> Father -> Son)
#3. Multiple Inheritance : Class A -> Class B, Class C -> Class B (Father -> Son, Mother -> Son)
"""
"""
# single Inheritance
class father:
    def __init__(self, f_house, f_car, f_business):
        self.father_home = f_house
        self.father_car = f_car
        self.father_business = f_business

    def show_father_house(self):
        print("Father House :", self.father_home)

    def show_father_car(self):
        print("Father Car:", self.father_car)

    def show_father_business(self):
        print("Father business:", self.father_business)

    def show_father_all_details(self):
        self.show_father_house()
        self.show_father_car()
        self.show_father_business()

# super method helps to initiate the constructor of parent class in the child class constructor
class son(father):
    def __init__(self, name, f_house, f_car, f_business):
        super().__init__(f_house, f_car, f_business)
        self.name = name

    def show_son_name(self):
        print("My name is:", self.name)

    
if __name__ == '__main__':
    obj = son('Jerry', 'Bangalow', 'Audi', 'Construction')
    obj.show_father_all_details()

"""


########## Multi Level Inheritance ###########
"""
# Multi Level Inheritance
class grandfather:
    def __init__(self, property):
        self.grand_father_property = property

    def show_grandfather_property(self):
        print("Grand father property:", self.grand_father_property)



class father(grandfather):
    def __init__(self, f_house, f_car, f_business, gfproperty):
        super().__init__(gfproperty)
        self.father_home = f_house
        self.father_car = f_car
        self.father_business = f_business

    def show_father_house(self):
        print("Father House :", self.father_home)

    def show_father_car(self):
        print("Father Car:", self.father_car)

    def show_father_business(self):
        print("Father business:", self.father_business)

    def show_father_all_details(self):
        self.show_father_house()
        self.show_father_car()
        self.show_father_business()
        self.show_grandfather_property()


# super method helps to initiate the constructor of parent class in the child class constructor
class son(father):
    def __init__(self, name, f_house, f_car, f_business, gfproperty):
        super().__init__(f_house, f_car, f_business, gfproperty)
        self.name = name

    def show_son_name(self):
        print("My name is:", self.name)


if __name__ == '__main__':
    obj = son('Jerry', 'Bangalow', 'Audi', 'Construction', '200 Acr')
    obj.show_father_all_details()
    obj.show_son_name()

"""


############## Multiple Inheritance #############
class mother:
    def __init__(self, mcar, mhouse, mbusiness):
        self.mcar = mcar
        self.mhouse = mhouse
        self.mbusiness = mbusiness

    def show_mother_details(self):
        print("mother car :", self.mcar)
        print("mother house :", self.mhouse)
        print("mother business :", self.mbusiness)


class father:
    def __init__(self, f_house='Banglow', f_car='Audi', f_business='Construction'):
        self.father_home = f_house
        self.father_car = f_car
        self.father_business = f_business

    def show_father_house(self):
        print("Father House :", self.father_home)

    def show_father_car(self):
        print("Father Car:", self.father_car)

    def show_father_business(self):
        print("Father business:", self.father_business)

    def show_father_all_details(self):
        self.show_father_house()
        self.show_father_car()
        self.show_father_business()

# super method helps to initiate the constructor of parent class in the child class constructor
# MRO : Method resolution order, priority of calling class will decide which method we can access
# sequence of class name will call , will decide the order.

class son(mother, father):
    def __init__(self, name, f_house, f_car, f_business, mcar, mhouse, mbusiness):
        super().__init__(mcar, mhouse, mbusiness)
        self.name = name
        self.fobj = father(f_house, f_car, f_business)

    def show_son_name(self):
        print("My name is:", self.name)


if __name__ == '__main__':
    obj = son('John', 'BeachHouse', 'Audi', 'fasion', 'BMW', '4BHK', 'BuetyProduct')
    print(obj.mcar)
    obj.show_mother_details()
    obj.fobj.show_father_all_details()



