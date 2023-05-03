import src.functions as func
from art import tprint


auction_dictionary = {}

tprint("silent auction")
print("Welcome to the silent auction program.")
func.auction_bidding(auction_dictionary)
highest_bidder = func.look_up_highest_bidder(auction_dictionary)
print(f"The winner is {highest_bidder} with a bid of ${auction_dictionary[highest_bidder]}.\n")
