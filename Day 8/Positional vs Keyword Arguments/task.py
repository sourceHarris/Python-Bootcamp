# # Functions with input
#
# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with_name("Haris", "Kohat")

def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left")


number = int(input("Enter your current age: "))

life_in_weeks(number)