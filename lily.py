#This is my WaterLily Dispatcher, it kinda calls my Waterlily VSC Feature
#I wrote all those comments so that you go ahead and inspect at home, cuz i know you are sneaky

#Imports for the handling
import sys

#from the storage folder we will import our command line interpretation
from storage.repo import init_repo, commit_changes
from storage.log import show_log
from storage.checkout import checkout_commit

#For the staging area commands
from storage.staging import add_file, remove_file

#Sys.argv helps read in the line commands
def main():
    if len(sys.argv) < 2:
        #If no arguement is passed, lily will show you it's methods
        print("Usage: python lily.py [init|commit|log|checkout]")
        return

    command = sys.argv[1]  
    # the first argument after "python lily.py" is treated as a command line

    #e.g Python lily.py init will create a lily folder for storing and tracking

    if command == "init":
            init_repo()
            #Init file explores this part better bro,
    elif command == "add":
            if len(sys.argv) < 3:
                print("Usage: python lily.py add <file>")
            else:
                add_file(sys.argv[2])
                #copies the file into .waterlily/stage/ 
    elif command == "rm":
            if len(sys.argv) < 3:
                print("Usage: python lily.py rm <file>")
            else:
                remove_file(sys.argv[2])
                #Removes files from stage area
    elif command == "commit":
            if len(sys.argv) < 3:
                print("Usage: python lily.py commit 'message'")
            else:
                commit_changes(sys.argv[2])
                #Futher explained in the commit part of the storage file 
    elif command == "log":
            show_log()
            #shows logs
    elif command == "checkout":
            if len(sys.argv) < 3:
                print("Usage: python lily.py checkout <commit_id>")
            else:
                checkout_commit(sys.argv[2])
                #Checkout or estore a snapshot
    else:
            print("Unknown command")

if __name__ == "__main__":
    main()