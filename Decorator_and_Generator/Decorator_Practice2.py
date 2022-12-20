def print_msg(msg):
    return msg

def greeting(func):
    print("Hey, how are you?")
    msg = func('I am doing good')
    print(msg)
    print("Good to hear that")

greeting(print_msg)



def greeting2(func):
    def inner(msg):
        print("this is first msg")
        print(func(msg))
        print('this is my second msg')
    return inner

@greeting2
def decorate_me(msg):
    return msg


#decorate_me("This is actual msg that is going to decorate")
import os

def create_fake_data():
    file_name = 'test_data.txt'
    from faker import Faker
    fk = Faker()

    with open(file_name, 'a') as file:
        for i in range(1000):
            first_name = fk.first_name()
            last_name = fk.last_name()
            email = fk.email()
            line = f"{first_name}, {last_name}, {email}\n"
            file.write(line)
    return file_name


def generate_fake_data(func):
    def inner(*args):
        filename = create_fake_data()
        func(filename)
        os.remove(filename)

    return inner


@generate_fake_data
def show_all_fake_data(filename):
    with open(filename, 'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            print(line)


show_all_fake_data()