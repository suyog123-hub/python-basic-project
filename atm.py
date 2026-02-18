print("Welcome to ATM machine")
BALANCE = 50000
PIN = 1234
MAX_ATTEMPTS = 5
MAX_TRANSACTION = 20000

attempts_left = MAX_ATTEMPTS
balance = BALANCE

while attempts_left > 0:
    try:
        user_pin = int(input("Enter your PIN code: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if user_pin == PIN:
        print("PIN accepted. Welcome!\n")
        
        while True:  
            print("\n1 --> Check balance")
            print("2 --> Withdraw amount")
            print("3 --> Deposit amount")
            print("4 --> Exit")
            
            try:
                choice = int(input("Please choose an option (1-4): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                print(f"Your current balance is: ${balance}")

            elif choice == 2:
                try:
                    amount = int(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > balance:
                    print("Insufficient funds.")
                elif amount > MAX_TRANSACTION:
                    print(f"Cannot withdraw more than ${MAX_TRANSACTION} per transaction.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful. New balance: ${balance}")

            elif choice == 3:
                try:
                    amount = int(input("Enter deposit amount: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > MAX_TRANSACTION:
                    print(f"Cannot deposit more than ${MAX_TRANSACTION} per transaction.")
                else:
                    balance += amount
                    print(f"Deposit successful. New balance: ${balance}")

            elif choice == 4:
                print("Thank you for using our ATM. Goodbye!")
                break   
            else:
                print("Invalid option. Please choose 1-4.")

        break   

    else:
        attempts_left -= 1
        if attempts_left == 0:
            print("Too many incorrect attempts. Your card is blocked.")
        else:
            print(f"Wrong PIN. Attempts left: {attempts_left}")