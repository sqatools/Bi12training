from OOPS3.python_list_class import pylist
from OOPS3.user_inputs import *

class common(pylist):

    def call_list_method(self):
        return self.get_square_of_all_numbers(list_square)


if __name__ == '__main__':
    obj = common()
    print(obj.get_even_keys_form(input_dict))
    print(obj.call_list_method())

