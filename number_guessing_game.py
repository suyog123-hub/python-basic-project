import random
print("Welcome to the Number Guessing Game! You have 3 attempts.")
comp_num = random.randint(0, 3)
attempts_left = 5
attempts_used = 0
while attempts_left > 0:
    try:
        guess = int(input("Enter a number from 0 to 3: "))
        if guess < 0 or guess > 3:
            print("Please enter a number between 0 and 3.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue
    attempts_used += 1
    attempts_left -= 1
    if guess < comp_num:
        print("Too low.")
    elif guess > comp_num:
        print("Too high.")
    else:
        print(f"Congratulations! You guessed the number in {attempts_used} attempt(s).")
        break

    if attempts_left > 0:
        print(f"You have {attempts_left} attempt(s) left.")
    else:
        print(f"Sorry, you've used all attempts. The number was {comp_num}.")