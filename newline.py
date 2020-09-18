import os

def help():
    print("Here CSV format means comma seperated values you can use excel to open these kinds of files")
    print("file_write : Will write data in the given file directory and deletes the previous data!")
    print("file_append : Will append/add data in the given file directory!")
    print("file_read : Will read data in the given file directory in a CSV format and return it in a list[list] format where each item of the list is a row!")
    print("folder_read : Will read data from the given folder directory in a CSV format!")
    print("read_line : Will read a specefic line in the CSV format file!")
    print("TIP : Give all data to write in List[List] format")

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

def read_line(file_dir:str,line:list):
    data = []
    for i in line:
        data.append(file_read(file_dir)[i-1])
    return data