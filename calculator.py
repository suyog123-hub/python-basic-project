print("🧮 SIMPLE CALCULATOR")

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    choice = input("Choose option: ")

    if choice == "5":
        print("👋 Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("❌ Cannot divide by zero")
    else:
        print("❌ Invalid choice")