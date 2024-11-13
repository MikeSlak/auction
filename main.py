import art
print(art.logo)

bidding_dictionary = {}

continue_bidding = True

while continue_bidding:
    name = input('What is your name? ')
    bid = input("What's your bid? $")

    bidding_dictionary[name] = int(bid)

    new_bid = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if new_bid == 'yes':
        print('\n' * 20)
        continue_bidding = True
    else:
        continue_bidding = False


highest_bidder = ""
highest_bid = 0

for key in bidding_dictionary:
    if bidding_dictionary[key] > highest_bid:
        highest_bidder = key
        highest_bid = bidding_dictionary[key]
print('\n' * 20)
print(f'The highest bidder was {highest_bidder} with a bid of ${highest_bid}')
