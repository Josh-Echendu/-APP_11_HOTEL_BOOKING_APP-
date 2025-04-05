import pandas as pd

# Load the frame and load the values the 'id' column as a string
df = pd.read_csv("005 hotels.csv", dtype={'id': str})

# load the values of all the column as strings and converted the csv file to a dictionary
df_cards = pd.read_csv('002 cards.csv', dtype=str).to_dict(orient='records')

df_cards_security = pd.read_csv('005 card-security.csv', dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
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
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content 

# Parent Class
class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, holder, cvc):
        print(df_cards)
        card_data = {'number': self.number, 'expiration': expiration,
                    'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        else:
            return False

# Child Class in terms of inheritance        
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False      

class SpaHotel():
    def __init__(self, spa_bool):
        self.spa_bool = spa_bool

    def book_spa_package(self):
        if self.spa_bool == 'yes':
            return True
        else:
            return False

class GenerateSpaTicket(SpaHotel):
    def generateticket(self, hotel_object, customer1_name):
        content = f"""
        Thank you for your SPA reservation!
        Here are your SPA booking data:
        Name: {customer1_name}
        Hotel name: {hotel_object.name}
        """
        return content

print(df)
hotel_ID = input("Enter the id of the hotel: ") 
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number= '12345678910')
    if credit_card.validate(expiration='12/26', holder='JOHN SMITH', cvc= '123'):
        if credit_card.authenticate(given_password= "mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name= name, hotel_object= hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want a Spa package?: ")
            spahotel = GenerateSpaTicket(spa_bool = spa)
            if spahotel.book_spa_package():
                print(spahotel.generateticket(hotel_object= hotel, customer1_name = name))
            else:
                print("Ok thanks for your response.")
        else:
            print("Credit card authentication failed.")  
    else:
        print('There was a problem with your payment.')

else:
    print("Hotel is not free.")    
