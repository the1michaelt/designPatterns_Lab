from logger import Logger
from order_factory import OrderFactory
from order import Order 

class Franchise:
    """ Utilize a Factory Pattern in the create_order() method 
    to instantiate instances of the three different Order child classes.
            Instantiate 3 separate Franchise objects .
        Call place_order on each franchise object multiple times.
        
        Use the Singleton pattern (as shown in the Design Patterns Demo repo) to create a single instance of a Logger object inside the logger.py file and import this instance into the Franchise class to be shared by all instantiations.   
    """    
    def __init__(self, location):
        self.location_number = location
      
    # Focus on instantiating the objects and passing in the location.

    def place_order(self):
        food_style_choices = ["North Indian","South Indian","Indian Asian Fusion"]
        order_placed = food_style_choices[(int(input(f'''\nHello! Thank you for dining at Indian Palace today!
        What style of Indian food do you have a taste for? 
        1: "North Indian"
        2: "South Indian"
        3: "Indian Asian Fusion"
        \n''')))-1]
        if food_style_choices == 1 or 2 or 3:
            order_proceed = OrderFactory.create_order(order_placed)
            transaction = Logger.log_transaction(Order)
       
        
    
