# This program is realted to files backup
# Author: Yash Vardhan
# Date: 02/11/2021

while True:

    # Printing The User Instructions

    print("Welcome To Our App!!")
    print("")
    print("Enter 1 For Files Mover (Moves The File From 1 Folder To Another)")
    print("Enter 2 For Copy Files Program (Copies The Files From 1 Folder To Another)")
    print("Enter 3 For Files Organizer (Organizes The Files based On Their File-Extension)")
    print("Enter 4 For Old Files Remover (Removes All The old Files)")
    print("Enter Q To Quit")
    print("")
    print("Note:- Choice means you have to choose one of the four programs based on your need. First read the user instructions carefully and then enter your choice.")

    # Making a choice Variable which will store the user's choice

    print("")
    choice = input("Enter Your Choice: ")

    # Executing The User's choice using if, elif statements

    if choice == 'Q':
        break

    elif choice == '1':

        # Files Mover Program

        print("")
        print("Files Mover Program")
        print("")
        # Importing The Necessary Modules

        import os
        import shutil

        source = input("Enter The Source Folder Name: ")
        destination = input("Enter The Destination Folder Name: ")

        source = source+'/'
        destination = destination+'/'

        list_of_files = os.listdir(source)

        for file in list_of_files:
            shutil.move((source+file), destination)
    
    elif choice == '2':

        # Copy Files Program
        print("")
        print("Copy Files Program")
        print("")
        # Importing The Necessary Modules

        import os
        import shutil

        source = input("Enter The Source Folder Name: ")
        destination = input("Enter The Destination Folder Name: ")

        source = source+'/'
        destination = destination+'/'

        list_of_files = os.listdir(source)

        for file in list_of_files:
            shutil.copy((source+file), destination)
    
    elif choice == '3':

        # File Organizer Program
        print("")
        print("Files Organizer Program")
        print("")

        # Importing The Necessary modules

        import os
        import shutil

        path = input("Enter The Name Of The Directory To Sort: ")

        list_of_files = os.listdir(path)

        for file in list_of_files:
            name,ext = os.path.splitext(file)
            ext = ext[1:]
            if ext == '':
                continue
            
            if os.path.exists(path+'/'+ext):
                shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
            
            else:
                os.makedirs(path+'/'+ext)
                shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    
    elif choice == '4':

        # Old Files Remover Program
        print("")
        print("Old Files Remover Program")
        print("")

        # Imporing The Necessary Modules
        import time
        import shutil

        path = input("Enter your path: ")

        days = 30
        seconds = time.time() - (days * 24 * 60 * 60)

        if os.path.exists(path):
            for root, dirs, files in os.walk(path, topdown=True):
                for name in files:
                    path = os.path.join(root, name)
                    ctime = os.stat(path).st_ctime

                    if seconds >= ctime:
                        os.remove(path)
                        print("\n Deleted the path " + path + " successfully")

                for name in dirs:
                    path = os.path.join(root, name)
                    ctime = os.stat(path).st_ctime

                    if seconds >= ctime:
                        shutil.rmtree(path)
                        print("\n Deleted the path " + path + " successfully")
        else:
            print("\n Path not found")
    else:
        print("Invalid Choice!! Please Try Again")