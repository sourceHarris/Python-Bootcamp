# import random
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# def deal_card():
#     return random.choice(cards)
#
# def calculate_score(score):
#     if 11 in score and sum(score) > 21:
#         score.remove(11)
#         score.append(1)
#         return sum(score)
#
#     elif sum(score) == 21:
#         return 0
#
#     else:
#         return sum(score)
#
#
# def compare(computer_total_score, user_total_score):
#     if computer_total_score == user_total_score:
#         print("Draw")
#     elif computer_total_score == 0:
#         print("You lose, opponent has Blackjack 😱")
#     elif user_total_score == 0:
#         print("Win with a Blackjack 😎")
#     elif user_total_score > 21:
#         print("You went over. You lose 😭")
#     elif computer_total_score > 21:
#         print("Opponent went over. You win 😁")
#     elif user_total_score > computer_total_score:
#         print("You win 😃")
#     else:
#         print("You lose 😤")
#
# def play_blackjack():
#     user = []
#     computer = []
#
#     for i in range(0, 2):
#         user.append(deal_card())
#     for i in range(0, 2):
#         computer.append(deal_card())
#
#     user_score = calculate_score(user)
#     computer_score = calculate_score(computer)
#
#     print(f"    Your cards: {user}, current score: {user_score}")
#     print(f"    Computer's first card: {computer[0]}")
#
#     if user_score  == 0 or computer_score == 0:
#         print("Game Over")
#
#     else:
#         another_card = input("Type 'y' to get another card, type 'n' to pass:   ").lower()
#
#         if another_card == "y":
#             user.append(deal_card())
#             user_score = calculate_score(user)
#
#     while computer_score != 0 and computer_score < 17:
#         computer.append(deal_card())
#         computer_score = calculate_score(computer)
#
#
#     print(f"    Your final hand: {user}, final score: {user_score}")
#     print(f"    Computer's final hand: {computer}, final score: {computer_score}")
#     compare(computer_total_score=computer_score, user_total_score=user_score)
#
#     compare(user_total_score=user_score, computer_total_score=computer_score)
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     play_blackjack()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "money": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

report = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
}

should_continue = True

while should_continue:
    def resources_checker(option):
        for key in MENU:
            if key == option:
                availability = ""
                for items in resources and MENU[option]["ingredients"]:
                    if resources[items] < MENU[option]["ingredients"][items]:
                        availability = items
                        print(f"Sorry there isn't enough {availability}")
                        return 0

        return 1
    def money_processor():
        if resources_checker(option=options) == 1:
            print("Please insert coin.")
            quarters = 0.25
            dimes = 0.10
            nickles = 0.05
            pennies = 0.01

            quarter = float(input("How many quarters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            pennie = float(input("How many pennies?: "))

            total_amount = round(float(quarter + dime + nickle + pennie))
            return total_amount
    def transaction_verification():
        actual_money = MENU[options]["cost"]
        inserted_money = money_processor()

        if inserted_money < actual_money:
            print(f"Sorry that's not enough money. Money refunded {inserted_money}$💸")
            return 0
        elif inserted_money == actual_money:
            report['money'] += actual_money
            print(f"Here is your {options} enjoy☕️")
            return 1
        elif inserted_money > actual_money:
            report['money'] += actual_money
            refund = inserted_money - actual_money
            print(f"Here is {refund}$ in change 💸")
            print(f"Here is your {options} enjoy☕️")
            return 1

    def make_coffee():
        if transaction_verification() == 1:
            ingredients = MENU[options]["ingredients"]

            for item in ingredients:
                report[item] -= ingredients[item]

    options = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if options == "off":
        print("Machine is shutting down...⏳")
        should_continue = False
    elif options == "report":
        for item in report:
            print("Here is the report ⚠")
            print(f"{item}: {report[item]}")
        should_continue = False
    elif options in MENU:
        make_coffee()
    else:
        print("Wrong choice")
        should_continue = False