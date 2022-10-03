import os

bid_list = []
def highest_bid(total_bidder):
    winner = {}
    for n in range(total_bidder):
        max_price = 0
        if bid_list[n]["bid_price"] > max_price:
            winner["max_name"] = bid_list[n]["name"]
            winner["max_bid"] = bid_list[n]["bid_price"]
    return winner
def add_bidder():
    bidder = {}
    bidder["name"] = input("What is your name?:")
    bidder["bid_price"] = int(input("What's your bid price: $")) 
    bid_list.append(bidder)   

print("Welcome to Silent Auction")
process = 'yes'
total_bidder = 0
while process != "no":
    add_bidder()
    total_bidder += 1
    process = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls')

winner = highest_bid(total_bidder)

print(f'The winner is {winner["max_name"]} with a bid of ${winner["max_bid"]}')
