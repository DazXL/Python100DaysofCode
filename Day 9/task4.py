# Task 4 is the Secret Auction Highest Bid Challenge
# Using dictionaries to store user input and compare values to find out who the highest bidder is and declaring the winner

# Some Variables
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


bids = {}
end_bids = False

print(logo) #Prints logo art.

# While Loop for entering keys and values to the Bids Dictionary.
while not end_bids:
    name = input("What is your name? \n")
    value =int(input("What is your bid?: $"))
    bids[name] = value
    answer = input("Are there any other bidders? Type 'yes' or 'no': \n")
    if answer == 'yes':
        print("\n" * 20)
    elif answer == 'no':
        end_bids = True # Ends the loop.

# Comparing the values in the dictionary to find out who is the highest bidder with a For Loop.
highest_bid_value = 0
winner_name = ""
for key in bids:

    if bids[key] > highest_bid_value:
        highest_bid_value = int(bids[key])
        winner_name = key

# Revealing the winner
print(f"The highest bid of the Action was '{winner_name}' with the value of '${highest_bid_value}'")
