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

def file_write(file_dir:str,content,v = True):
    if v:
        print("WARNING : This function will write whatever content is in the parameter and wipe the existing data!")
    with open(file_dir,"w+") as f:
        for i in content:
            for k in range(0,len(i)):
                f.write(str(i[k]))
                if k != len(i)-1:
                    f.write(",")
            f.write("\n")
    return "File Overwritten"

def file_append(file_dir:str,content,v = True):
    if v:
        print("This Function will add data to existing function!")
    with open(file_dir,"a+") as f:
        for i in content:
            for k in range(0,len(i)):
                f.write(str(i[k]))
                if k != len(i)-1:
                    f.write(",")
            f.write("\n")
    return "File Overwritten"

file_append("C:\\Users\\Ayush Sharma\\Desktop\\Programs\\newline_test.txt",[[1,2,3],[2,3],[3,4],[5,6]],True)