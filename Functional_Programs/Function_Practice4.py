#from Functional_Programs.Function_Practice3 import addition
from Functional_Programs.Function_Practice3 import *

output = addition(150, 60)
print(output)

output2 = multiplication(5, 6)
print(output2)

def check_given_number_is_prime(num):
    """ This function will check the given number is
    prime or not
    :param num: input number which is provided by user
    :return:
    """
    prime = True
    for i in range(2, num):
        if num%i == 0:
            prime = False
            break
        else:
            continue
    return prime

print(check_given_number_is_prime(11))

print(check_given_number_is_prime.__doc__)
