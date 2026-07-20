# main.py

from inventory import *
from file_handler import *


def menu():

    while True:

        print("\n====== INVENTORY MANAGEMENT SYSTEM ======")

        print("1.Add Product")
        print("2.View Products")
        print("3.Search Product")
        print("4.Update Product")
        print("5.Delete Product")
        print("6.Update Stock")
        print("7.Low Stock Alert")
        print("8.Inventory Value")
        print("9.Save Data")
        print("10.Load Data")
        print("11.Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_product()

        elif choice == 2:
            view_products()

        elif choice == 3:
            search_product()

        elif choice == 4:
            update_product()

        elif choice == 5:
            delete_product()

        elif choice == 6:
            update_stock()

        elif choice == 7:
            low_stock()

        elif choice == 8:
            inventory_value()

        elif choice == 9:
            save_data()

        elif choice == 10:
            load_data()

        elif choice == 11:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


menu()