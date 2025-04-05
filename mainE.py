import pandas as pd

# Load the frame and load the values the 'id' column as a string
df = pd.read_csv("005 hotels.csv", dtype={'id': str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

        # Extracting the name of the Hotel in strings
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()



    def book(self):
        """Book a hotel by changing its availability to no, if already booked"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('005 hotels.csv', index=False) # we use the index=False, bcos we do not want python to create another index


    def available(self):
        """Check if hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):

        # Created an attribute 
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content 
    

print(df)
hotel_ID = input("Enter the id of the hotel: ") 
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name= name, hotel_object= hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")     


# Implement the Methods of the Reservation Ticket Class   

