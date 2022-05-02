import json
import tkinter

#Function to print file information
def print_file(file_name):
    fi = open(file_name)
    with open(file_name, 'r') as fi:
        data = json.load(fi)
    print(data)
    fi.close()

def main():
    file_name = input("Enter your JSON file name: ")
    print_file(file_name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

