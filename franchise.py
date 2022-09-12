from logger import logger
from order_factory import OrderFactory

class Franchise:
    """ Utilize a Factory Pattern in the create_order() method 
    to instantiate instances of the three different Order child classes.
            Instantiate 3 separate Franchise objects .
        Call place_order on each franchise object multiple times.
    """    
    def __init__(self, number, options):
        self.location_number = number
        self.options = options
    
        
    def place_order(self):
        food_style_choices = [1, 2, 3]      
        order_placed = food_style_choices[(int(input('''\nHello! Thank you for dining at Indian Palace today!
        What style of Indian food do you have a taste for? 
        1: "North Indian, $22"
        2: "South Indian, $22"
        3: "Indian Asian Fusion, $26"
        \n'''))) - 1]
    
        if food_style_choices == 0 or 1 or 2:
            return order_placed #user makes a choice
        else:
            self.place_order() #repeat until user enters a valid choice
    
    def order_location(self):
        location_number = [1, 2, 3]      
        order_location = location_number[(int(input('''Where would you like to buy your food? 
        1: "Brooklyn"
        2: "Queens"
        3: "Manhattan"
        '''))) - 1]
    
        if order_location == 0 or 1 or 2:
            return order_location #user makes a choice
        else:
            self.order_location()  # repeat until user enters a valid choice
    
        # use the static Factory method to get an OBJECT based on what choice the user made
        # # depending on what number is typed in for order_placed, call the Factory method and pass in the appropraite string
        
        # The place_order() method should:
        #     call the static OrderFactory.create_order() method to instantiate an order object.
        #     call the logger.log_transaction() method to log the order to the log.txt file
 
