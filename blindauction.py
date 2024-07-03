print("===================================================WELCOME TO BLIND AUCTION=============================================================================")

from art import logo

print(logo)

import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    
bids = {}
bidding_finished = False 

def find_highest_bidder(bidding_record) :
  highest_bid = 0 
  winner = " "
  for bidder in bidding_record : 
     bid_amount = bidding_record[bidder]
     if bid_amount > highest_bid :
        highest_bid = bid_amount
        winner = bidder
  print(f"The winner is {winner} the bid is ${highest_bid}") 
  print("The Auction is closed\nThank You for Coming")


while not bidding_finished :
  name = input("What is your name : ")
  price = int(input("What is your bid?\n$"))
  bids[name] = price
  bidders = input("Are there any other bidders?\nType 'yes' or 'no'.\n").lower()
  if bidders == 'no' : 
    bidding_finished = True
    find_highest_bidder(bids)
  elif bidders == 'yes' :
    clear_console()