# from ast import main
from franchise import Franchise
# main

class Simulation:
    """create a Simulation class with a run_simulation() method to act as a facade pattern.
    The run_simulation() method should: 
        Instantiate 3 separate Franchise objects.
        Call place_order on each franchise object multiple times.            
    """

    def __init__(self):
        pass

    def run_simulation(self): #instantiates an order by each (of the three) locations
        location1_order = Franchise(1)
        location2_order = Franchise(2)
        location3_order = Franchise(3)
        
        location1_order.place_order()
        location2_order.place_order()
        location1_order.place_order()
        location2_order.place_order()
        location3_order.place_order()
        location3_order.place_order()

  
