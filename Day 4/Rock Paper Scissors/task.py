import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors."))
computer = random.randint(0, 2)

if user == computer:
    print("It's a draw")

elif user == 0 and computer == 2:
    print("User wins")

elif user == 2 and computer == 1:
    print("User wins")

elif user == 1 and computer == 0:
    print("User wins")

else:
    print("You lose")

print(f"You chose {choice[user]}")
print(f"Computer chose {choice[computer]}")