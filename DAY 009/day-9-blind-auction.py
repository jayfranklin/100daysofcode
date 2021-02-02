from replit import clear
#HINT: You can call clear() to clear the output in the console.

from auction_art import logo
print(logo)

# Create new dictionary for bids to be stored
bids = {}

def add_bid(name, bid):
  bids[name] = bid

# While loop
continue_running = True
while continue_running:
  # Prompt user for name, bid, and whether to add additional bidders
  bidder = input("What is your name? ")
  amount = int(input("What is your bid? $"))
  new_bidder = input("Are there any additional bidders? Type 'yes' or 'no'.")
  add_bid(bidder, amount)

  #print(bids)

  if new_bidder == "no":
    continue_running = False
  clear()


def highest_bidder(bid):
  highest_bid = 0
  winner = ""
  for person in bid:
    amount = bid[person]
    if amount > highest_bid:
      highest_bid = amount
      winner = person
  print(f"The highest bidder is {winner} with a bid of ${highest_bid}")

# Determine the winner
highest_bidder(bids)


# Alternative to iterating the dictionary
#

'''  # Original method splitting the dictionary into lists, sorting to find the max value, 
         finding the index of that value in original list, and using the value of max index
         to find the original key value, which would be the winning bidder

# Split dictionary into two lists, keys and values
key_list = list(bids.keys())
value_list = list(bids.values())

# Determine highest bidder 
# sort the values into ascending order
value_list_sorted = sorted(value_list)
#print(value_list_sorted)

# Determine the highest bid by referencing the last index
high_bid = value_list_sorted[-1]
#print(high_bid)

# Find the index of the value_list that references the highest bid
high_bid_value = value_list.index(high_bid)
#print(high_bid_value)

# Use the value_list index to deterine they key in the dictionary
winner = key_list[high_bid_value]
#print(winner)

# Finally, print the winner and their bid

print(f"The highest bid was {winner} with ${high_bid}")



    
'''
