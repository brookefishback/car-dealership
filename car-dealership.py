#So you two are going to deliver a Car Dealership Sales Management solution that adheres to the following requirements:
#1. Maintains a database of customers who have interacted with sales, including name and phone number
#2. Sells at least 1 model of vehicle with at least 5 customizable options. These options can either be chosen as part of a trim level, or fully customized.
#3. The result of the sales process should be a screen that displays a work order for the vehicle - basically just a list of the options to be included. Think like an order ticket at a restaurant, so the vehicle can be built.

import random

#CREATE CLASS - COMPOSED OF CUSTOMER INFO AND CAR CUSOMIZTATIONS
class Order:
    def __init__(self, name, number, color, trim, tint, rims, sunroof):
        self.name = name
        self.number = number
        self.color = color
        self.trim = trim
        self.tint = tint
        self.rims = rims
        self.sunroof = sunroof

order_list = [
    Order("Brooke", "817-733-6342", "black", "black", "black", "big", "auto"),
    Order("Brooke", "214-532-1965", "brown", "grey", "white", "small", "auto")
]

#CREATE ORDER FUCNTION - TAKES SALESMAN INPUT TO CREATE WORKORDER FOR CUSTOMER'S DESIRED VEHICLE
def create_order(self):

    name = input("Enter customer name: ")
    number = input("Enter phone number: ")
    color = input("Enter color: ")
    trim = input("Enter trim color: ")
    tint = input("Enter tint level: ")
    rims = input("Enter rim size: ")
    sunroof = input("Enter sunroof type: ")
    completed_order = Order(name, number, color, trim, tint, rims, sunroof)
    order_list.append(completed_order)

    #USE COUNTER TO DETERMINE ORDER NUMBER
    print("Order has been added to the database.")
    print(completed_order.name)
    print(completed_order.number)
    print(completed_order.color)
    print(completed_order.trim)
    print(completed_order.tint)
    print(completed_order.rims)
    print(completed_order.sunroof)

#CREATE VIEW ORDER FUCNTION - PRINTS ORDER LIST FOR SALESMAN
def view_orders():
    for order in order_list:
        print(order.number)

#CRRATE MAIN MENU FUNTION
def main():
    menu = {}
    menu['1']="Add Order" 
    menu['2']="View Orders"
    menu['3']="Exit"

#WHILE AND IF STATEMENTS TO HANDLE SALESMEN'S MENU CHOICES
user=True
while user:
    print ("""
    1.Add an Order
    2.View Orders
    3.Exit/Quit
    """)
    answer=input("What would you like to do? ") 
    if answer=="1": 
        create_order(Order)
    elif answer=="2":
        view_orders()
    elif answer=="3":
        print("\n Goodbye")
        break
    elif answer !="":
        print("\n Invaild Entry")

if __name__ == "__main__":
    main()
