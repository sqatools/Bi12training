import os, sys
import shutil

"""
# Get current working directory
cur_dir= os.getcwd()
print("current directory path:", cur_dir)

# Get all files and folder list
"""
data = os.listdir("E:\\Filesdata")
print(data)
"""

# Create directory
#os.mkdir('TestFolder') # current directory

#os.mkdir("E:\\Filesdata\\BI12\\NewFolder")

# Remove folder from target directory
#os.removedirs("E:\\Filesdata\\new_dir\\BI10")

# join method to join two path
"""
#path1 = "E:\\Filesdata"
#path2 = "Bi12"

#output = os.path.join(path1, path2)
#print(output)

#os.mkdir(output)
"""

# Check given path is file
filepath = "E:\\Filesdata\\count_name1.txt"
print(os.path.isfile(filepath))

# Check given path is directory

dirpath = "E:\\Filesdata\\Bi13"
print(os.path.isdir(dirpath))

# Copy file from one location to another

src_path = "E:\\Filesdata\\count_name.txt"
tar_path = "E:\\Filesdata\\Bi12\\count_name_copied.txt"

shutil.copy(src_path, tar_path)
# run os command in python script

#os.system("control")
#os.system("appwiz.cpl")


#
print(sys.platform)
print(sys.path)

# get environment variable data
print(os.getenv('Browser'))
print(os.getenv('path'))
"""
# Get extension count each type of file on the given target location

def get_extension_count(tar_path="E:\\Filesdata"):
    output = {}
    # Get all the file/folder list
    data_list = os.listdir(tar_path)
    # Apply loop in list data and get each file/folder one by one
    for data in data_list:
        #print(data)
        # Get path each file/folder
        data_path = os.path.join(tar_path, data)
        print(data_path)
        # Check the data path is file or not
        if os.path.isfile(data_path):
            file_ext = data.split(".")[1]
            #print (data, file_ext)
            if file_ext in output:
                output[file_ext] += 1
            else:
                output[file_ext] = 1
    return output
print(get_extension_count())


