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

    # Class method  
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)    


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):# This is an instance method
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    


hotel1 = Hotel(hotel_id='188')
hotel2 = Hotel(hotel_id='655')

# Calling an intsance method
print(hotel1.available())

# Caliing the class method

print(hotel1.get_hotel_count(data= df))
print(Hotel.get_hotel_count(data= df))

# you use the class method, when you need to a method that is somehow related to a class
# but not related to an instance, that is when you use the class method