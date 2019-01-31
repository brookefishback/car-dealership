#So you two are going to deliver a Car Dealership Sales Management solution that adheres to the following requirements:
#1. Maintains a database of customers who have interacted with sales, including name and phone number
#2. Sells at least 1 model of vehicle with at least 5 customizable options. These options can either be chosen as part of a trim level, or fully customized.
#3. The result of the sales process should be a screen that displays a work order for the vehicle - basically just a list of the options to be included. Think like an order ticket at a restaurant, so the vehicle can be built.

import random
from datetime import datetime

#CREATE CLASS - COMPOSED OF CUSTOMER INFO AND CAR CUSOMIZTATIONS
class Order:
    def __init__(self, name, number, color, trim, tint, rims, sunroof, transaction, time):
        self.name = name
        self.number = number
        self.color = color
        self.trim = trim
        self.tint = tint
        self.rims = rims
        self.sunroof = sunroof
        self.transaction = transaction
        self.time = time

order_list = [
    Order("Brooke", "817-733-6342", "black", "black", "black", "big", "auto", "1",""),
    Order("Noah", "214-532-1965", "black", "white", "smokey", "18s", "manual","2","")
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
    transaction = transaction_number()
    time = time_and_date_stamp()
    completed_order = Order(name, number, color, trim, tint, rims, sunroof, transaction, time)
    order_list.append(completed_order)

    #USE COUNTER TO DETERMINE ORDER NUMBER
    print()
    print(completed_order.time)
    print("Transaction number: " + str(completed_order.transaction) + " has been added to the database.")
    print("Name: " + str(completed_order.name))
    print("Phone Number: " + str(completed_order.number))
    print("Car Color: " + str(completed_order.color))
    print("Trim Color: " + str(completed_order.trim))
    print("Tint Level: " + str(completed_order.tint))
    print("Rim Size: " + str(completed_order.rims))
    print("Sunroof: " + str(completed_order.sunroof))

#CREATE VIEW ORDER FUCNTION - PRINTS ORDER LIST FOR SALESMAN
def view_orders():
    for order in order_list:
        print("Order Number: " + str(order.transaction)), 
        print("Name: " + str(order.name)), 
        print("Phone Number: " + str(order.number))
        print()

#CRRATE MAIN MENU FUNTION
def main():
    menu = {}
    menu['1']="Add Order" 
    menu['2']="View Orders"
    menu['3']="Exit"

#CREATE TIME STAMP
def time_and_date_stamp():
    today_date = datetime.now()
    return today_date

#CREATE ORDER NUMBER
def transaction_number():
    transaction_order = len(order_list) + 1
    return transaction_order

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
