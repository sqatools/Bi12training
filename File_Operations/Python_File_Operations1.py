def read_file_content(filename='test_read.txt'):
    with open( filename, "r") as file:
        # read specific byte data
        #data = file.read(10)
        #print(data)

        # read specific line of the file
        """
        file_line = file.readline()
        print(file_line)
        """
        # read 5 lines
        """
        for i in range(5):
            file_line = file.readline()
            print(file_line, end="")
        """

        # Read list of lines
        file_lines = file.readlines()
        print(file_lines)
        for line in file_lines:
            print(line, end="")

#read_file_content()

# Read last 2 lines of the file

def read_last_2lines(filename='test_read.txt'):
    with open( filename, "r") as file:
        file_lines = file.readlines()
        last_two_lines = file_lines[-2:]

        for line in last_two_lines:
            print(line, end="")

#read_last_2lines()

# move file lines which are divide by 3 to next file

def mode_file_data(filename="test_read.txt", tar_file="tarfile.txt"):
    with open( filename, "r") as file:
        temp = ''
        file_lines = file.readlines()
        for i in range(len(file_lines)):
            if (i+1)%3 == 0:
                temp = temp + file_lines[i]
            else:
                continue

    with open(tar_file, "w") as file:
        file.write(temp)


# mode_file_data()
# Write a python program to move even lines and odd lines in two different file
# Write a python get all the email id from given file.
# Write a python program to replace word 'Python' with 'Java'
# Write a python program to get all the mobile numbers from given file.



def replace_word(word1, word2, filename= "classword_read.txt"):
    with open(filename, "r") as file:
        data = file.read()

    data = data.replace(word1, word2)

    with open(filename, "w") as file:
        file.write(data)

#replace_word("Python", "Java")

# seek method : we can set  cursor position with the help of seek method
# tell method : this method return current position of the cursor

def read_content_set_cursor(filename = "classword_read.txt"):
    with open(filename, "rb") as file:
        # initial cursor position
        output1 = file.tell()
        print("initial position:", output1)
        byte10 = file.read(20)
        print("byte10:", byte10)
        output2 = file.tell()
        print("cursor position after 10 char:", output2)
        #file.seek(40, 0)  # set cursor position from begining of the file
        #file.seek(40, 1)   # set cursor position from current position of the cursor
        file.seek(-50, 2)
        print("cursor position after its position:", file.tell())
        output3 = file.read()
        print("output3 :", output3)


read_content_set_cursor()

# Project :
"""
Write a python project to maintain employee details
-> data will in form of dict
id_1={"name": "rahul", "email":"rahul@gmail.com", "phone":345678}

-> add employee details
-> remove employee details
-> update employee details
-> get specific employee details with id
-> get all employee details
"""