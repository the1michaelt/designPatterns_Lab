# from order import Order
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
        self.daily_sales = 0
        self.transaction_count = 0
        
    def log_transaction(self, Order, location_number):
        self.transaction_count += 1  # each transaction increases the count by one
        self.daily_sales += self.food_price  # add order price to the daily sales
        activity = open("log.txt", "a")  # Open the text document
        activity.write(
            f'{self.transaction_count}: {self.food_style} at {location_number}-- {self.food_price} Total: {daily_sales}\n')
        activity.close()  # Remember to close the file
        
        
        
      # order_placed # the number of the product
        # order_location # number of the location
        
    #Call one time        
    
      
        

####
# from chat_history import chat_history

# class User:
#     def send_message(self, message):
#         chat_history.messages.append(message)

# from user import User
# user_one = User()
# user_two = User()

# location1_order.write_to_log(Order)
# location2_order.write_to_log(Order)
# location3_order.write_to_log(Order)
# user_two.send_message("Hi.")
# user_one.send_message("What are you doing this weekend?")
# user_two.send_message("Camping in the Rocky Mountains.")
# user_one.send_message("Sounds exciting. Be safe!")
# chat_history.display_history()
    