import os


def ask_for_name_bidder():
    """Use standard input to ask for the name of the bidder and return that value."""
    name = input("What is your name?: ")
    return name


def ask_for_bidding_amount():
    """Use standard input to ask for the bid amount and return that value."""
    amount = input("What's your bid?: $")
    return amount


def add_to_auction_dictionary(bidder_name, bid_amount, auction_dictionary):
    """Add bid name and bid amount to auction dictionary."""
    auction_dictionary[bidder_name] = bid_amount
    return auction_dictionary


def auction_bidding(auction_dictionary):
    """Use while loop to add biddings to auction dictionary."""
    end_bidding = False
    while not end_bidding:
        bidder_name = ask_for_name_bidder()
        bid_amount = ask_for_bidding_amount()
        auction_dictionary = add_to_auction_dictionary(bidder_name, bid_amount, auction_dictionary)
        end_bidding = ask_to_end_bidding()
        os.system('cls||clear')
    return auction_dictionary

       
def ask_to_end_bidding():
    """Use standard input to ask the bidding to stop."""
    result = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if result != "yes":
        end_bidding = True
    else:
        end_bidding = False
    return end_bidding


def look_up_highest_bidder(auction_dictionary):
    """Go through each bid in auction dictionary and return the highest bidder."""
    highest_bid = 0
    for key in auction_dictionary:
        bid_amount = float(auction_dictionary[key])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bidder_name = key
    return bidder_name
