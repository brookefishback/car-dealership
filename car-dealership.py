#So you two are going to deliver a Car Dealership Sales Management solution that adheres to the following requirements:
#1. Maintains a database of customers who have interacted with sales, including name and phone number
#2. Sells at least 1 model of vehicle with at least 5 customizable options. These options can either be chosen as part of a trim level, or fully customized.
#3. The result of the sales process should be a screen that displays a work order for the vehicle - basically just a list of the options to be included. Think like an order ticket at a restaurant, so the vehicle can be built.

class Customer:
    def __init__(self, customer_name, interested_car, phone_number="555-5555"):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.interested_car = interested_car
        self.car_to_order = ''

class Sedan:
    def __init__(self, sedan_tint="no tint", sedan_transmission="auto", sedan_engine="v4", sedan_trim="silver", sedan_seats="cloth"):
        self.sedan_tint = sedan_tint
        self.sedan_transmission = sedan_transmission
        self.sedan_engine = sedan_engine
        self.sedan_trim = sedan_trim
        self.sedan_seats = sedan_seats

class Luxury:
    def __init__(self, luxury_seats="warmers", luxury_cameras="backup", luxury_roof="sunroof", luxury_trim="blackout", luxury_rims="18s"):
        self.luxury_seats = luxury_seats
        self.luxury_cameras = luxury_cameras
        self.luxury_roof = luxury_roof
        self.luxury_trim = luxury_trim
        self.luxury_rims = luxury_rims

customer_sales_list = []
sedan_list = []
luxury_list = []

def sample_sedan():
    print("----Adding sample sedan model.----")
    template_sedan = Sedan()
    print(template_sedan.sedan_tint)
    print(template_sedan.sedan_transmission)
    print(template_sedan.sedan_engine)
    print(template_sedan.sedan_trim)
    print(template_sedan.sedan_seats)
    sedan_list.append(template_sedan)

sample_sedan()
print(sedan_list)

def sample_luxury():
    print("----Adding sample luxury model.----")
    template_luxury = Luxury()
    print(template_luxury.luxury_seats)
    print(template_luxury.luxury_cameras)
    print(template_luxury.luxury_roof)
    print(template_luxury.luxury_trim)
    print(template_luxury.luxury_rims)
    luxury_list.append(template_luxury)

sample_luxury()
print(luxury_list)

def sample_clients():
    print("----Sample Client One----")
    customer_one = Customer("John Smith", "sedan")
    print(customer_one.customer_name)
    print(customer_one.phone_number)
    print(customer_one.interested_car)
    customer_sales_list.append(customer_one)

    print("----Sample Client Two----")
    customer_two = Customer("Jane Doe", "luxury", "123-4567")
    print(customer_two.customer_name)
    print(customer_two.phone_number)
    print(customer_two.interested_car)
    customer_sales_list.append(customer_two)

sample_clients()
print(customer_sales_list)

#Creating new client and car, either sedan or luxury.
def new_car_client():
    customer_name = input("Client's name: ")
    interested_car = input("Sedan or Luxury: ")
    phone_number = input("Phone number: ")
    client_sedan_buyer = Customer(customer_name, interested_car, phone_number)

    if interested_car == "Sedan":
        print("Please input the desired Sedan specs. Hit Enter to select default.")
        new_client_sedan_tint = input("No Tint, upgrade to: ")
        new_client_sedan_transmission = input("Automatic transmission, change to: ")
        new_client_sedan_engine = input("Default is v4, upgrade to: ")
        new_client_sedan_trim = input("Silver trim is standard, upgrade to: ")
        new_client_sedan_seats = input("Cloth seats, upgrade to: ")
        client_ordered_sedan = Sedan(new_client_sedan_tint, new_client_sedan_transmission, new_client_sedan_engine, new_client_sedan_trim, new_client_sedan_seats)

        client_sedan_buyer.car_to_order = client_ordered_sedan

        print(client_sedan_buyer.customer_name), print(client_sedan_buyer.interested_car), print(client_sedan_buyer.phone_number)
        print(client_ordered_sedan.sedan_tint), print(client_ordered_sedan.sedan_transmission), print(client_ordered_sedan.sedan_engine), print(client_ordered_sedan.sedan_trim), print(client_ordered_sedan.sedan_seats)

#def returning_car_client():

while True:
    print("Python Car Dealership.")
    dealer_input = input("Is this an RETURNING customer or NEW?")
    if dealer_input == "New":
        new_car_client()
#    elif dealer_input == "Returning":
#        returning_car_client():
#    else:
#    return

        