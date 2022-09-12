class Logger:
    def __init__():
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
        pass

    def log_transaction(self):
        self.daily_sales: #int
        self.transaction_count: #int
            
    def write_to_log(word):
        file = open("log.txt", "a")
        file.write("Sales for today are {word}!\n")
        file.close()

    write_to_log("evening!")
    