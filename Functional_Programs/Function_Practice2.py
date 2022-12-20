"""
##### Variable scope #####

Global Variable : Variable that we defined outside of the function then it is known as
global variable. and the scope of global variable is available across the modules.

-> if you want to change global variable value in the function, then we have to use
global keyword. e.g global varx

Local Variable : variable that we defined in the function is known as local variable
and its scope limited to the function only.

NonLocal Variable: non-variable is scope is limited to all the inner of the outer function.
"""

# Global Variable
varx = 60

def show_values():
    vary = 70  # Local Variable
    varx = 100 # Local Variable
    print("varx :", varx)
    print("vary :", vary)

def show_values3():
    global varx
    vary = 70  # Local Variable
    varx = 200 # Local Variable
    print("varx :", varx)
    print("vary :", vary)


def show_values2():
    varz = 100 # Local Variable
    print("varx :", varx)
    print("varz :", varz)

show_values()
print("_"*50)
show_values3()
print("_"*50)
varx = 700
show_values2()

# Write python program to get max value from list

"""
def get_max(list1):
    max_value = 0
    for var in list1:
        if var > max_value:
            max_value = var

    print("max value :",  max_value)


# Call by value
#get_max([5, 8, 2, 9, 12, 56, 27])
# call by reference
listp = [1, 6, 23, 77, 8, 14, 38]
#get_max(listp)
get_max(list1=listp)


def get_max_len_word(str1):
    max_len_word = ''
    max_len = 0
    word_list = str1.split()

    for word in word_list:
        word_len = len(word)
        if word_len > max_len:
            max_len = word_len
            max_len_word = word

    print("Max len Word :", max_len_word)

get_max_len_word("Hello Very Good Morning fgfgdfgdfgdsgf")
"""

# non local variable


g_var = 600  # global variable

def outer():
    nl_var = 700 # non local variable

    def inner_fun1():
        print("Its inner function1")
        l_var = 800 # local variable
        print("global variable:", g_var)
        print("non local variable:", nl_var)
        print("local variable:", l_var)

    def inner_fun2():
        print("Its inner function2")
        nonlocal nl_var
        global g_var

        nl_var = 1000
        g_var = 1200
        l_var2 = 900 # local variable
        print("global variable:", g_var)
        print("non local variable:", nl_var)
        print("local variable:", l_var2)

    inner_fun1()
    print("_"*50)
    inner_fun2()
    print("_" * 50)
    inner_fun1()

outer()

