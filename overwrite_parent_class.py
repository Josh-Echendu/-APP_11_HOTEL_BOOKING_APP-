class Ticket:
    def __init__(self):
        pass
    def generate(self):
        return "Hello, this is your ticket"
    

class DigitalTicket(Ticket):
    def download(self):
        pass
    
    # We want to overwrite the generate method in the Ticket class
    def generate(self):
        return "Hi this is your ticket"

dt = DigitalTicket()
print(dt.generate())

t = Ticket()
print(t.generate())
# Note when you inherit from class, you do not modify the parent class you only modify the parent class