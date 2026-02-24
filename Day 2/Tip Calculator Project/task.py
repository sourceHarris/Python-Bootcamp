print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage = tip / 100

tip_amount = percentage * bill

grand_total = bill + tip_amount

final_bill = grand_total / people

print(f"The final bill will be {final_bill}")