import os

def file_read(file_dir:str):
    with open(file_dir,"r") as f:
        data = f.read()
        f.close()
    data = data.split("\n")
    seperated_data = []
    for i in data:
        seperated_data.append(i.split(","))
    return seperated_data

def folder_read(folder_dir:str):
    files = os.dir(folder_dir)
    content = []
    for f in files:
        content.append(file_read(dir + "//" + f))
    return content


print(file_read("newline.txt"))