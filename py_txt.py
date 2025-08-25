import os
import shutil
import sys

def txt_py(file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
   
    if file_name.lower()=="r":
        old_file_name = str(input("Old file name: "))
        new_file_name = str(input("New file name: "))
        if os.path.isfile(old_file_name):
            os.rename(old_file_name, new_file_name)
        return False
   
    elif file_name.lower()=="rm":
        name = input("File name: ")
        if os.path.exists(name) and os.path.isfile(name):
            os.remove(name)
        return False
    
    elif file_name.lower()=="rdir":
        old_folder_name = str(input("Old folder (dir) name: "))
        new_folder_name = str(input("New folder (dir) name: "))
        if os.path.exists(old_folder_name) and os.path.isdir(old_folder_name):
            os.rename(old_folder_name, new_folder_name)
        return False
    
    elif file_name.lower()=="mkdir":
        new_folder_name = str(input("New folder (dir) name: "))
        os.mkdir(new_folder_name)
        return False

    elif file_name.lower()=="rmdir":
        try:
            name = input("Folder name: ")
            if not name:
                print("| -~- Error! No directory name provided. -~- |")
                return False
            CAREFUL_NOW = input("WARNING: Are you sure you want to delete the contents of this directory? (y or n): ")
            if os.path.exists(name) and os.path.isdir(name):
                if CAREFUL_NOW.lower()=="y":
                    shutil.rmtree(name)
                elif CAREFUL_NOW.lower()=="n":
                    return False
                else:
                    print("Please enter y or n next time.")
        except OSError:
            print(f"| -~- Error! {name} is NOT empty. -~- |")
        except PermissionError:
            print("| -~- Error! Please check required permission. -~- |")
        return False
    
    elif file_name.lower()=="ls":
        print("Current directory content: ")
        b = os.listdir()
        b = '\n'.join(b)
        print(b)
        specific = input("Would you like to list a specific directory in your directory? (y or n): ")
        if specific.lower()=="y":
            try:
                direct = input("Directory name: ")
                a = os.listdir(direct)
                a = '\n'.join(a)
                print(f"Contents of {direct}:\n{a}")
            except OSError as ose:
                print(f"| -~- Error! {ose}. -~- |")
        elif specific.lower()=="n":
            return False
        return False

    elif file_name.lower()=="i":
        print(f"\nJSONreader")
        print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
        print(f"Being imported: Yes\nFile path: {__file__}")
        return False

    if not os.path.isfile(file_name):
        write = input("")
        with open(file_name, 'x') as file:
            file.write(write)
   
    else:
        with open(file_name, 'r') as file:
            txt = file.read()
            print(txt)
   
    while True:
        write = input("")
   
        if write == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
   
        with open(file_name, 'a') as file:
            file.write("\n" + write)

print("r - Rename file\nrm - Delete file\nmkdir - Create new folder\nrdir - Rename directory\nrmdir - Delete folder")
print("ls - List contents of a directory\ni - Info")
name_of_file = str(input("Enter file name to make new file, edit or enter one of the modes above: "))
txt_py(name_of_file)