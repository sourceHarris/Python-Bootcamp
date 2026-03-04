# TODO-1: Ask the user for input
dictionary = {}

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added


game_continue = True
score = 0
highest_bidder = ""

while game_continue:
    user = input("What is your name?: ").lower()
    bid = int(input("what is your bid?: "))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if more_bidders == "no":
        game_continue = False
    elif more_bidders == "yes":
        print("\n" * 20)

    dictionary[user] = user
    dictionary[user] = bid

for entry in dictionary:

    if dictionary[entry] > score:
        score = dictionary[entry]
        highest_bidder = entry
# TODO-4: Compare bids in dictionary


print(dictionary)
print(f"{highest_bidder} is the winner")