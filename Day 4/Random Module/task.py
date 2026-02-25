import random

coin = random.randint(0, 1)

print(coin)

if coin == 0:
    print("It's a head")
else:
    print("It's a tail.")