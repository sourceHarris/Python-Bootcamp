# TODO-1: Ask the user for input
dictionary = {}

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added


game_continue = True
score = 0

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
        score = dictionary[entry]

        if dictionary[entry] > score:
            dictionary[entry] = score
        elif score > dictionary[entry]:
            print(f"{entry} is the winner!")
# TODO-4: Compare bids in dictionary


print(dictionary)