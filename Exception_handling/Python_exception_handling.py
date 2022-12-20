"""
try:
    num1 = 123
    output = num1/0
    print(output)
except Exception as e:
    print("division by zero is not allowed")
    print(e)

"""

"""
try:
    num1 = 456
    str1 = 'Hello'
    output = num1 + str1
except Exception as e:
    print("addition of int and string is not allowed")
    #print(e)
    raise
"""
# try -> except -> else : If there is no exception in the program then else condition will
# be executed.
"""
try:
    num1 = 40
    num2 = 50
    print("addition:", num1 + num2)
except Exception as e:
    print(f"some is broken : {e}")
else:
    output = num1 + num2
    print("multiply value:", output*2)
"""

# try -> except -> finally: code present finally block always executes even there is exception
# or not exception in the code.
"""
list1 = [7, 8, 2, 9, 2]
list2 = ['a', 'b', 567, 23]
try:
    for val in list1:
        print(val, ":", val**2)

    assert sum(list1) == 50
    with open("readfile.txt", 'r') as file:
        data = file.write("File")
        print(data)

except AssertionError:
    print("Assertion Error")
except IOError:
    print("IO Error")
except ArithmeticError:
    print("Arithmetic Error")

finally:
    print("_"*40)
    for val in list2:
        print(val, ":", val*2)

"""

# try -> except -> else -> finally
# else condition only executes when there is no exception in the code
"""
list1 = [7, 8, 2, 9, 2]
list2 = ['a', 'b', 567, 23]
try:
    for val in list1:
        print(val, ":", val**2)

    assert sum(list1) == 50
    with open("readfile.txt", 'r') as file:
        data = file.read()
        print(data)

except AssertionError:
    print("Assertion Error")
except IOError:
    print("IO Error")
except ArithmeticError:
    print("Arithmetic Error")
else:
    print("There is exception in the code")

finally:
    print("_"*40)
    for val in list2:
        print(val, ":", val*2)

"""

# Nested exception
num1 = 10
num2 = 40
try:
    print("we are first exception block")
    print("addition :", num1 + num2)
    try :
        print("we are in second exception block")
        print("division :", num1/0)


    except Exception as e:
        print("second exception raised:", e)

except Exception as var:
    print("first exception raised:", var)




