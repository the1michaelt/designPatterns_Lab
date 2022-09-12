from chat_history import chat_history
from order import order
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
        
        # order_placed # the number of the product
        # order_location # number of the location
        # transaction_count +=1  #each transaction increases the count by one
        # self.daily_sales += order_placed.price #add order price to the daily sales
        
            
    def write_to_log(word):
        activity = open("log.txt", "a")
        activity.write(f"{transaction_count}: {order_placed} at {order_location}-- {order_price} Total: {daily_sales}\n")
        activity.close()
        activity.write_to_log(word)  # this?

    write_to_log("great")

####
# from chat_history import chat_history

# class User:
#     def send_message(self, message):
#         chat_history.messages.append(message)

# from user import User

# user_one = User()
# user_two = User()

# user_one.send_message("Hello.")
# user_two.send_message("Hi.")
# user_one.send_message("What are you doing this weekend?")
# user_two.send_message("Camping in the Rocky Mountains.")
# user_one.send_message("Sounds exciting. Be safe!")
# chat_history.display_history()
    