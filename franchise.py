from logger import Logger
from order_factory import OrderFactory

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
        food_style_choices = [1, 2, 3]      
        order_placed = food_style_choices[(int(input(f'''\nHello! Thank you for dining at Indian Palace today!
        What style of Indian food do you have a taste for? 
        1: "North Indian, $22"
        2: "South Indian, $22"
        3: "Indian Asian Fusion, $26"
        \n'''))) - 1]
        # if food_style_choices == 0 or 1 or 2:
        #     return order_placed #user makes a choice
        # else:
        #     self.place_order() #repeat until user enters a valid choice
        
        order_proceed = OrderFactory.create_order(order_placed)
        transaction = Logger()
        transaction.log_transaction(OrderFactory)
        # transaction.log_transaction(OrderFactory, location_number)
        
    # def place_order(self):
    #     food_style_choices = [1, 2, 3]
    #     order_placed = food_style_choices[(int(input(f'''\nHello! Thank you for dining at Indian Palace today!
    #     What style of Indian food do you have a taste for? 
    #     1: "North Indian, $22"
    #     2: "South Indian, $22"
    #     3: "Indian Asian Fusion, $26"
    #     \n'''))) - 1]
    #     if food_style_choices == 0 or 1 or 2:
    #         return order_placed  # user makes a choice
    #     else:
    #         self.place_order()  # repeat until user enters a valid choice

    #     log_transaction = Logger()
    #     log_transaction.log_transaction()



  #single instance of a Logger object inside the logger.py file and import this instance into the Franchise class to be shared by all instantiations
   #     call the logger.log_transaction() method to log the order to the log.txt file


         
     # use the static Factory method to get an OBJECT based on what choice the user made
        # # depending on what number is typed in for order_placed, call the Factory method and pass in the appropraite string
        
        # The place_order() method should:
        #     call the static OrderFactory.create_order() method to instantiate an order object.
    
