# from sys import stdout
from sys import exit
import texttable as tt


# Command line program to create a Receipt generating Grocery Store
class Store(object):
    store_name = "Utsav General Store"
    cart_items = []
    cart_quantity = []
    cart_price = []
    user_name = "preethi"
    user_password = "admin123"

    def __init__(self, name, password):
        self.name = name
        self.password = password

    # print_total function will calculate the cart total and display the total
    def print_total(self):
        price_sum = 0
        for price in Store.cart_price:
            price_sum = price_sum + price
        rupee_symbol = u"\u20B9"
        print "CART TOTAL = ", rupee_symbol, price_sum

    # print_receipt function is used to print the receipt for the consumer
    def print_receipt(self, name):
        print "\n\t\t\t\tReceipt"
        print "-" * 40
        print "Consumer Name:", name.upper()
        print "-" * 40
        display_table = tt.Texttable()
        headings = ['Item Name', 'Quantity', 'Price']
        display_table.header(headings)
        for row in zip(Store.cart_items, Store.cart_quantity, Store.cart_price):
            display_table.add_row(row)
        view_table = display_table.draw()
        print (view_table)
        self.print_total()

    # login function is used to display all the categories of items to the user
    def login(self, name, password):
        if name == Store.user_name and password == Store.user_password:
            print "-" * 40
            print "\t\t\tWELCOME ", name.upper()
            my_choice = 1
            while my_choice:
                print "-" * 40
                print "CATEGORIES"
                print "-" * 40
                print "1) Food Items\n2) Drinks\n3) Groceries\n4) Stationaries\n5) Fashion\n6) Exit"
                print "-" * 40
                category_choice = int(raw_input("Enter your choice:"))
                if category_choice == 1:
                    print "-" * 40
                    print "List of food items:"
                    print "-" * 40
                    print "1) Bread\n2) Pizza\n3) Sandwich\n4) Burger"
                    print "-" * 40
                    item_choice = int(raw_input("Enter your choice:"))
                    quantity = int(raw_input("Enter the quantity:"))
                    if item_choice == 1:
                        Store.cart_items.append("Bread")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 15)
                    elif item_choice == 2:
                        Store.cart_items.append("Pizza")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 90)
                    elif item_choice == 3:
                        Store.cart_items.append("Sandwich")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 30)
                    elif item_choice == 4:
                        Store.cart_items.append("Burger")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 30)
                    else:
                        print "-" * 40
                        print "Invalid choice...Check your input again"
                    print "-" * 40
                elif category_choice == 2:
                    print "-" * 40
                    print "List of Drinks:"
                    print "-" * 40
                    print "1) Frooti\n2) Sprite\n3) Fanta\n4) Zaffa"
                    print "-" * 40
                    item_choice = int(raw_input("Enter your choice:"))
                    quantity = float(raw_input("Enter the quantity in litre:"))
                    if item_choice == 1:
                        Store.cart_items.append("Frooti")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 25)
                    elif item_choice == 2:
                        Store.cart_items.append("Sprite")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 25)
                    elif item_choice == 3:
                        Store.cart_items.append("Fanta")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 27)
                    elif item_choice == 4:
                        Store.cart_items.append("Zaffa")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 25)
                    else:
                        print "-" * 40
                        print "Invalid choice...Check your input again"
                    print "-" * 40
                elif category_choice == 3:
                    print "-" * 40
                    print "List of Groceries:"
                    print "-" * 40
                    print "1) Red Chilly\n2) Coriander seeds\n3) Sugar\n4) Salt"
                    print "-" * 40
                    item_choice = int(raw_input("Enter your choice:"))
                    quantity = float(raw_input("Enter the quantity in kg:"))
                    if item_choice == 1:
                        Store.cart_items.append("Red Chilly")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 85)
                    elif item_choice == 2:
                        Store.cart_items.append("Coriander seeds")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 60)
                    elif item_choice == 3:
                        Store.cart_items.append("Sugar")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 45)
                    elif item_choice == 4:
                        Store.cart_items.append("Salt")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 20)
                    else:
                        print "-" * 40
                        print "Invalid choice...Check your input again"
                    print "-" * 40
                elif category_choice == 4:
                    print "-" * 40
                    print "List of Stationaries:"
                    print "-" * 40
                    print "1) Book\n2) Pen\n3) Pencil\n4) Eraser"
                    print "-" * 40
                    item_choice = int(raw_input("Enter your choice:"))
                    quantity = int(raw_input("Enter the quantity:"))
                    if item_choice == 1:
                        Store.cart_items.append("Book")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 45)
                    elif item_choice == 2:
                        Store.cart_items.append("Pen")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 15)
                    elif item_choice == 3:
                        Store.cart_items.append("Pencil")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 6)
                    elif item_choice == 4:
                        Store.cart_items.append("Eraser")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 10)
                    else:
                        print "-" * 40
                        print "Invalid choice...Check your input again"
                    print "-" * 40
                elif category_choice == 5:
                    print "-" * 40
                    print "\nList of Fashion items:"
                    print "-" * 40
                    print "1) T-Shirt\n2) Jeans\n3) Sweater\n4) Raincoat"
                    print "-" * 40
                    item_choice = int(raw_input("Enter your choice:"))
                    quantity = int(raw_input("Enter the quantity:"))
                    if item_choice == 1:
                        Store.cart_items.append("T-Shirt")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 250)
                    elif item_choice == 2:
                        Store.cart_items.append("Jeans")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 500)
                    elif item_choice == 3:
                        Store.cart_items.append("Sweater")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 450)
                    elif item_choice == 4:
                        Store.cart_items.append("Raincoat")
                        Store.cart_quantity.append(quantity)
                        Store.cart_price.append(quantity * 900)
                    else:
                        print "-" * 40
                        print "Invalid choice...Check your input again"
                    print "-" * 40
                elif category_choice == 6:
                    break
                else:
                    print "-" * 40
                    print "Invalid choice...Check your input again"
                    print "-" * 40
                print "Do you want to continue shopping?"
                my_choice = int(raw_input("If YES press 1...If NO press 0 >"))
                if my_choice == 0:
                    self.print_receipt(username)
                    exit(0)
        else:
            print "-" * 40
            print "Username or password is incorrect"


# outside the Store class
login_choice = 1
while login_choice:
    print "-" * 40
    string = "LOGIN"
    print string.center(40)
    print "-" * 40
    username = raw_input("Enter the user name: ")
    password1 = raw_input("Enter the password: ")
    store_object = Store(username, password1)
    if username == Store.user_name and password1 == Store.user_password:
        print "-" * 40
        print "\tWELCOME TO ", Store.store_name.upper()
        store_object.login(username, password1)
    else:
        print "-" * 40
        print "Invalid username or password"
        print "-" * 40
    print "Do you want to login again?"
    login_choice = int(raw_input("If YES press 1...if NO press 0 >"))


