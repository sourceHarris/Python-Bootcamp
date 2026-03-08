import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []

def deal_card():
    return random.choice(cards)

for i in range(0, 2):
    user.append(deal_card())
for i in range(0, 2):
    computer.append(deal_card())

def calculate_score(score):

    if 11 in score and sum(score) > 21:
        score.remove(11)
        score.append(1)
        return sum(score)

    elif sum(score) == 21:
        return 0

    else:
        return sum(score)

user_score = calculate_score(user)
computer_score = calculate_score(computer)

print(f"    Your cards: {user}, current score: {user_score}")
print(f"    Computer's first card: {computer[0]}")

def compare(computer_total_score, user_total_score):
    if computer_total_score == user_total_score:
        print(f"    Your cards: {user}, current score: {user_score}")
        print(f"    Computer's first card: {computer[0]}")
        print("Draw")
    elif computer_total_score == 0:
        print(f"    Your cards: {user}, current score: {user_score}")
        print(f"    Computer's first card: {computer[0]}")
        print("You loose")
    elif user_total_score == 0:
        print(f"    Your cards: {user}, current score: {user_score}")
        print(f"    Computer's first card: {computer[0]}")
        print("You win")
    elif user_total_score > 21:
        print(f"    Your cards: {user}, current score: {user_score}")
        print(f"    Computer's first card: {computer[0]}")
        print("You loose")
    elif computer_total_score > 21:
        print(f"    Your cards: {user}, current score: {user_score}")
        print(f"    Computer's first card: {computer[0]}")
        print("You win")

    restart = input("Do you want to restart the game? type 'y' for yes and 'n' for no: ").lower()

if user_score  == 0 or computer_score == 0:
    print("Game Over")

else:
    another_card = input("Type 'y' to get another card, type 'n' to pass:   ").lower()

    if another_card == "y":
        user.append(deal_card())
        user_score = calculate_score(user)

while computer_score != 0 and computer_score < 17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)


compare(user_total_score=user_score, computer_total_score=computer_score)