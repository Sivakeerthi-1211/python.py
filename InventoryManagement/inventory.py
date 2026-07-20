# inventory.py

from products import products


def add_product():
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    product = {
        "id": pid,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product Added Successfully.")


def view_products():
    print("\nID\tName\t\tPrice\tQuantity")
    print("-"*45)

    for p in products:
        print(p["id"], "\t", p["name"], "\t", p["price"], "\t", p["quantity"])


def search_product():
    pid = int(input("Enter Product ID: "))

    for p in products:
        if p["id"] == pid:
            print(p)
            return

    print("Product Not Found")


def update_product():
    pid = int(input("Enter Product ID: "))

    for p in products:
        if p["id"] == pid:

            p["name"] = input("New Name: ")
            p["price"] = float(input("New Price: "))
            p["quantity"] = int(input("New Quantity: "))

            print("Product Updated")
            return

    print("Product Not Found")


def delete_product():
    pid = int(input("Enter Product ID: "))

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            print("Product Deleted")
            return

    print("Product Not Found")


def update_stock():

    pid = int(input("Enter Product ID: "))

    for p in products:

        if p["id"] == pid:

            print("1. Purchase")
            print("2. Sale")

            choice = int(input("Choice: "))

            qty = int(input("Enter Quantity: "))

            if choice == 1:
                p["quantity"] += qty

            elif choice == 2:
                if qty <= p["quantity"]:
                    p["quantity"] -= qty
                else:
                    print("Insufficient Stock")

            print("Stock Updated")
            return

    print("Product Not Found")


def low_stock():

    print("\nLow Stock Products\n")

    for p in products:

        if p["quantity"] < 5:
            print(p)


def inventory_value():

    total = 0

    for p in products:
        total += p["price"] * p["quantity"]

    print("Total Inventory Value =", total)