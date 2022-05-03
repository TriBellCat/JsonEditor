import json
import sys

#Function to print file information
def read_file(file_name):
    fi = open(file_name)
    with open(file_name, 'r') as fi:
        data = json.load(fi)
    print(data)
    fi.close()

#Function to write and create a file if it doesn't exist
def write_file(file_name):

    contLoop = True
    object_list = []
    data_list = []
    user_dict = {}

    #A while loop that asks the user to input the data
    while contLoop:
        object = input("Enter object: ")
        object_list.append(object)
        data = input("Enter data: ")
        data_list.append(data)

        print("Do you want to add another object? (True/False)")
        user_loop = input()
        if user_loop == 'True' or user_loop == 'true':
            contLoop = True
        elif user_loop == 'False' or user_loop == 'false':
            contLoop = False

    #Adds the two lists to a dictionary
    user_dict = {object_list[i]: data_list[i] for i in range(len(object_list))}

    #Converts the Python object into JSON objects and writes it to the user's file
    with open(file_name, 'w') as fi:
        json.dump(user_dict, fi, sort_keys=True, indent=4)

    print("File has been created and written to.")
    fi.close()

#Appends .json to file name if the user did not input it
def append_extension(file_name, choice):
    choice = 1
    string_fn = str(file_name)
    x = []
    sep = ""

    # Checks if file_name does not end with .json and appends .json to the end of it
    if not string_fn.endswith("."):
        x.append(".")
    if not string_fn.endswith("json"):
        x.append("json")
    file_name = f"{string_fn}{sep.join(x)}"

    if int(choice) == 1:
        check_valid(file_name)
        read_file(file_name)
    elif int(choice) == 2:
        write_file(file_name)

#Checks if json file exists
def check_valid(file_name):
    try:
        fi = open(file_name)
    except IOError:
        sys.exit("File does not exist")

def main():
    cont_loop = True

    while cont_loop:
        file_name = input("Enter your JSON file name: ")
        print("What do you want to do with the file?")
        print("1. Read information from file")
        print("2. Write to file")
        user_option = input()

        if int(user_option) == 1:
            read_file(file_name)
        elif int(user_option) == 2:
            write_file(file_name)
        else:
            print("Invalid option!")

        print("Do you want to do anything else? (True/False)")
        user_loop = input()
        if user_loop == 'True' or user_loop == 'true':
            cont_loop = True
        elif user_loop == 'False' or user_loop == 'false':
            cont_loop = False

if __name__ == '__main__':
    main()

