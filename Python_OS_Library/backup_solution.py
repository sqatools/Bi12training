import os, shutil
src_path = "E:\\filedata_srcdata\\1000files"
tar_path = "E:\\target_location"

def get_data_list(src_path):
    data_list = os.listdir(src_path)
    return data_list

#print(get_data_list(src_path))

def get_files_path(src_path):
    # {'txt' : [path, path1]}
    path_dict = {}
    data_list = get_data_list(src_path)
    for data in data_list:
        data_path = os.path.join(src_path, data)
        if os.path.isfile(data_path):
            file_ext = data.split(".")[1]
            if file_ext in path_dict:
                path_dict[file_ext].append(data_path)
            else:
                path_dict[file_ext] = [data_path]

        else:
            continue
    return path_dict

#print(get_files_path(src_path))

def copy_data_src_tar(src_path, tar_path):
    files_path = get_files_path(src_path)
    for ext, files_paths_list in files_path.items():
        print(ext, ":", files_paths_list)
        folder_path = os.path.join(tar_path, ext)
        print(folder_path)
        if os.path.isdir(folder_path):
            pass
        else:
            os.makedirs(folder_path)
        for path in files_paths_list:
            print(path)
            filename = path.split("\\")[-1]
            file_tar_path =  os.path.join(folder_path, filename)
            #print(file_tar_path)
            #print("_"*50)

            shutil.copy(path, file_tar_path)

copy_data_src_tar(src_path, tar_path)