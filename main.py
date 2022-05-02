import json

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
    while (contLoop):
        object = input("Enter object: ")
        object_list.append(object)
        data = input("Enter data: ")
        data_list.append(data)

        user_loop = input("Do you want to end another object? (True/False) ")
        if user_loop == 'True' or user_loop == 'true':
            contLoop = True
        elif user_loop == 'False' or user_loop == 'false':
            contLoop = False

    #Adds the two lists to a dictionary
    user_dict = {object_list[i]: data_list[i] for i in range(len(object_list))}

    #Converts the Python object into JSON objects and writes it to the user's file
    with open(file_name, 'w') as fi:
        json.dump(user_dict, fi)

    print("File has been created and written to.")

def main():
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

if __name__ == '__main__':
    main()

