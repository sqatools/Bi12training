"""
obj = open("filename/filepath", "filemode")
mode:
1. read mode (r): we can read the content of the existing file with read mode.
2. write mode (w)
3. append mode (a)
"""
# Read content of the file
"""
file_obj = open("test_read.txt", "r")
data = file_obj.read()
print("filename :", file_obj.name)
print("File mode :",  file_obj.mode)
print(data)
file_obj.close()
"""


# Write content to the file
# Case1 : If file does not exist : when we open file with write mode, then it
#         will create new file and add content to the file

"""
str1 = "Hello Good Morning , Its very fresh day"
file_obj = open("test_write1.txt", "w")
file_obj.write(str1)
file_obj.close()
"""
# Case2 : If file already exist : when we open file with write mode, then it
#         will overwrite the existing content of the file.

# str1 = "We are overwriting content of the file"
# file_obj = open("test_write2.txt", "w")
# file_obj.write(str1)
# file_obj.close()

# Create python file
"""
str1 = "print('Hello World')"
file_obj = open("test_programs.py", "w")
file_obj.write(str1)
file_obj.close()
"""

# Create different extension files
"""
file_ext = ['txt', 'png', 'xls', 'mp3', 'java', 'csv']

for ext in file_ext:
    for i in range(1, 11):
        filename = f"test_file_{i}.{ext}"
        str1 = "5438y43285345"*100
        file_obj = open(f"test_data\\{filename}", "w")
        file_obj.write(str1)
        file_obj.close()
"""

# Write content to the file with append mode
# case1: If file doest not exist, then  append mode will create new file and
#        add content to the file
"""
str1 = "print('Hello World')"
file_obj = open("append_content.txt", "a")
file_obj.write(str1)
file_obj.close()
"""

# case2: If file already exist, then  append mode will
#        add content to the file at the end.
"""
str1 = "\n Its new content that we are adding"
file_obj = open("append_content2.txt", "a")
file_obj.write(str1)
file_obj.close()
"""

# Open image and its content
"""
str1 = "\n Its new content that we are adding"
file_obj = open("Inheritance_diagram2.png", "rb")
data= file_obj.read()
print(data)
file_obj.close()
"""

# Context Manger : it has its own enter and exit method, so no need to close the file specifically,
"""
with open("test_read.txt", "r") as file:
    data = file.read()
    print(data)
"""

# Open file for with read and write operation with r+
"""
str1 = "We are adding content with read mode\n"
with open("test_read.txt", "r+") as file:
    data = file.write(str1)
    print(data)
"""


# Open file for with read and write operation with w+
# We can not read content , entire data will be overwrite with write mode
"""
str1 = "We are adding content with read mode\n"
with open("test_read.txt", "w+") as file:
    data = file.read()
    print(data)
"""

str1 = "We are adding content with read mode\n"
with open("test_read.txt", "a+") as file:
    data = file.read()
    print(data)
