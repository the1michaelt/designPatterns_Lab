from order import Order
from north_indian import NorthIndianFare  #necessary for the static method below
from south_indian import SouthIndianFare
from indo_asian import IndoAsianFusion   

class OrderFactory:
    """
    FACTORY DESIGN PATTERN
    Create an Order Factory class with a static create_order method.
    This method should accept a string as a parameter (ex “Pizza” or whatever food) 
    and return the corresponding type of Order child class instantiation (ex Pizza() )
    """         
    @staticmethod
    def create_order(self, order_placed): #string; Order is the parameter? 
        """ Based on the input value (the order), an object is created (the type of food)
        """        
        if order_placed == 0:
            return NorthIndianFare()  #STATIC METHOD-- method called off the class itself
        elif order_placed == 1:
            return SouthIndianFare()
        else: 
            return IndoAsianFusion()

       
       
        