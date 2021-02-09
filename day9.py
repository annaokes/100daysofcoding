## Dictionary Project
import os

bid_list={}
def create_bid_list():

  others_in_bid_queue = True
  while others_in_bid_queue:
    print("Welcome to the Silent Bidding Auction")
    user_name = str(input("What is your name?: "))
    user_bid = int(input("What is your bid?: £"))
    bid_list[user_name] = user_bid
    other_bidders = str(input("Are there any other bidders, please type yes or no: "))
    if other_bidders == 'yes':
        others_in_bid_queue = True
        os.system('clear')
    else:
      others_in_bid_queue = False
      os.system('clear')
      max_name = max(bid_list, key=bid_list.get)
      all_values = bid_list.values()
      max_value = max(all_values)
      print(f'The winner with the highest bid is {max_name} with £{max_value}')


create_bid_list()
print(bid_list)