import random

choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choice2 = random.randint(1, 3)
print(f"Computer chose: {choice2}")
if choice1 == choice2:
    print("Draw")
elif choice1 == 0 and choice2 == 1:
    print("You lose")
elif choice1 == 0 and choice2 == 2:
    print("You win")
elif choice1 == 1 and choice2 == 0:
    print("You win")
elif choice1 == 1 and choice2 == 2:
    print("You lose")
elif choice1 == 2 and choice1 == 0:
    print("You lose")
else:
    print("You win")
