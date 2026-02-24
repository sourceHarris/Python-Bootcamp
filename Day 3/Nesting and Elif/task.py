print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
#
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age?: "))

    if age < 12:
        bill = 5
    elif age >= 12 and age <= 18:
        bill = 7
    elif age > 18:
        bill = 12

    want_photo = input("Do you also want photos?: (y/n)").lower()

    if want_photo == "y":
        bill += 3
    print(f"Please pay {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
