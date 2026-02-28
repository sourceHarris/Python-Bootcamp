# Functions with input
#
# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with_name(name="Haris", location="Kohat")

# Kohatdef life_in_weeks(age):
#     weeks_left = (90 - age) * 52
#     print(f"You have {weeks_left} weeks left")
#
#
# number = int(input("Enter your current age: "))
#
# life_in_weeks(number)

def calculate_love_score(name1, name2):
    word_true = "true"
    word_love = "love"

    true_counter = 0
    love_counter = 0

    #Looping through word "TRUE" for name 1
    for i in word_true:
        for j in name1:
            if i == j:
                true_counter += 1

    # Looping through word "LOVE" for name 1
    for i in word_love:
        for j in name1:
            if i == j:
                love_counter += 1

    # Looping through word "TRUE" for name 2
    for i in word_true:
        for j in name2:
            if i == j:
                true_counter += 1

    # Looping through word "LOVE" for name 2
    for i in word_love:
        for j in name2:
            if i == j:
                love_counter += 1


    print(f"Love Score = {true_counter}{love_counter}")


first_name = input("Enter first name: ").lower()
second_name = input("Enter second name: ").lower()


calculate_love_score(name1=first_name, name2=second_name)