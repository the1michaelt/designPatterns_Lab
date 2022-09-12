class Logger:
    def __init__(self):
        """create a Logger class with a log_transaction() method 
        that will accept an Order object and store number and:
            Increase the Logger’s transaction_count by one
            Add the price of the Order object to the Logger’s daily income
            Open the log.txt file
            
            Write a well-formatted message to the log.txt file containing the current transaction count, 
            the name of the dish ordered, the store it was ordered from, the price of the item, 
            and the combined daily income.
            
             Use the Singleton pattern (as shown in the Design Patterns Demo repo) to create 
             a single instance of a Logger object inside the logger.py file and 
             import this instance into the Franchise class to be shared by all instantiations.
        """        

    def log_transaction(self, sales, count):
        self.daily_sales = sales
        self.transaction_count = count
        
        order_placed # the number of the product
        order_location # number of the location
        transaction_count +=1  #each transaction increases the count by one
        self.daily_sales += order_placed.price #add order price to the daily sales
        
            
    def write_to_log(word):
        file =open("log.txt", "a")
        file.write("Sales for today are {word}!\n")
        file.close()

    write_to_log("great")
    