expenses = []

while True:
    print("\n1.Add Expense 2.View Total 3.Exit")
    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Category: ")
        expenses.append({"amount": amount, "category": category})

    elif choice == "2":
        total = sum(e["amount"] for e in expenses)
        print("Total Spent:", total)

    elif choice == "3":
        break