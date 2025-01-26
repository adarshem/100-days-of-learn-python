from art import logo
from utils import clear_terminal

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


def find_highest_bidder(bidding_record):
    # We could use the max function to find the highest bid - max(bidding_record, key=bidding_record.get)
    # max function to get both key and value - max(bidding_record.items(), key=lambda x: x[1])
    
    # However, we will loop through the dictionary to find the highest bidder
    # compare the bids and fine the highest bidder
    highest_bid = 0
    highest_bidder = ""
    for key in auction_dictionary:
        if auction_dictionary[key] > highest_bid:
            highest_bid = int(auction_dictionary[key])
            highest_bidder = key

    print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")

# Starting the program with the logo
print(logo)

# Initialize the dictionary
auction_dictionary = {}
# Initialize the continue_bidding variable
continue_bidding =  True

# Loop through the program until the user decides to stop
while continue_bidding:
    bidder_name = str(input("What is your name: "))
    bidder_amount = int(input("Enter your bid amount: $"))
    auction_dictionary[bidder_name] = bidder_amount
    should_continue_bidding = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    clear_terminal()
    if should_continue_bidding== 'no':
        continue_bidding = False
        find_highest_bidder(auction_dictionary)
    else:
        print("Please continue bidding....")       



