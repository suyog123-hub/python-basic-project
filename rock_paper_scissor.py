import random

user = input("Enter your choice (R, P, S): ").upper()
computer = random.choice(['R', 'P', 'S'])

print("User:", user)
print("Computer:", computer)

if (user == 'S' and computer == "P") or \
   (user == 'P' and computer == "R") or \
   (user == 'R' and computer == "S"):
    print("You win")

elif user == computer:
    print("It's a draw")

else:
    print("You lose")