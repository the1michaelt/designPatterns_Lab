from order import Order

class SouthIndianFare(Order):
    """Child class
    """
    def __init__(self, name, price):
        super().__init__()
        self.dish_name = name
        self.price = price