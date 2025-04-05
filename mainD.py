import pandas as pd

# Load the frame and load the values the 'id' values as a string
df = pd.read_csv("005 hotels.csv", dtype={'id': str})

class Hotel:
    def __init__(self, hotel_id):
        # Created attribute of this method
        self.hotel_id = hotel_id


    def book(self):
        """Book a hotel by changing its availability to no, if already booked"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'

        # Update, save and overwrite  the changes to the csv file
        df.to_csv('005 hotels.csv', index=False) # we use the index=False, bcos we do not want python to create another index


    def available(self):
        """Check if hotel is available"""

        # Extracting the strings from the dataframe which is either  yes or no
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass   


print(df)
hotel_ID = input("Enter the id of the hotel: ") 
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("Hotel is not free.")    

# Implement the Methods of the Hotel Class