import os
def file1():
    try:
        if os.path.exists("demo.txt"):
            os.remove("demo.txt")
            print("file is deleted")
        else:
            print("File doesn't Exist")
    except:
            print("please Enter Correct Filename")

file1()
