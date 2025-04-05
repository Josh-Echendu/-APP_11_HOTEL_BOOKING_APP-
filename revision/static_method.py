import pandas

df = pandas.read_csv(r"\Users\hp\Music\pythonprojects\PYTHON_60_DAYS\APP_11_HOTEL_BOOKING_APP\005 hotels.csv", dtype={"id": str})


class Hotel:
    water_mark = "The real estate Company" # This is a class variable

    def __init__(self, hotel_id): # This is an instance method
        self.hotel_id = hotel_id # This is an instance variable
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()# This is an instance variable

    def book(self): # This is an instance method

        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no" # This is an instance variable
        df.to_csv("hotels.csv", index=False)

    def available(self):# This is an instance method
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze() # This is an instance variable
        if availability == "yes":
            return True
        else:
            return False
        

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):# This is an instance method
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod
    def convert(amount):
        return amount * 1.2

hotel1 = Hotel(hotel_id='188')
hotel2 = Hotel(hotel_id='655')

converted = ReservationTicket.convert(10)
print(converted)
