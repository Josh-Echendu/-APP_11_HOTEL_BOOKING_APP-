import pandas as pd

df = pd.read_csv("005 hotels.csv")

class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    # This method is going toreturn a boolean 
    def available():
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass
    
    # This generate the user_ticket
    def generate(self):
        pass


print(df)

id = input("Enter the id of the hotel: ") 

# Created instance of hotel
hotel = Hotel(id)

# Check if hotel is avialable we 
if hotel.available():
    hotel.book()

    # Get customer name
    name = input("Enter your name: ")

    # Created a reservation_ticket instance and passed
    # the hotel instance and name as argument
    
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("Hotel is not free.")    

# Create instances