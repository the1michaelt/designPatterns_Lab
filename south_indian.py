from order import Order

class SouthIndianFare(Order):
    """Child class, South Indian
    """
    def __init__(self):
        super().__init__("South Indian", 24)
     