# file_handler.py

from products import products


def save_data():

    file = open("inventory.txt", "w")

    for p in products:
        file.write(str(p) + "\n")

    file.close()

    print("Data Saved Successfully")


def load_data():

    try:

        file = open("inventory.txt", "r")

        print("\nStored Data\n")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No Saved Data Found")