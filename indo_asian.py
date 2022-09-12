from order import Order

class Indo_AsianFusion(Order):
    """Child class
    """    
    
    def __init__(self, name, price):
        super().__init__()
        self.dish_name = name
        self.price = price