from logger import logger
from order_factory import order_factory

class Franchise:
    """ Utilize a Factory Pattern in the create_order() method 
    to instantiate instances of the three different Order child classes.
    """    
    def __init__(self):
        pass
    
    def place_order(self):
        """ create a Simulation class with a run_simulation() method to act as a facade pattern. 
        The run_simulation() method should:
             ask a user what food they would like to order
            call the static OrderFactory.create_order() method to instantiate an order object.
            call the logger.log_transaction() method to log the order to the log.txt file
        """        
        self.location_number
