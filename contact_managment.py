print('----' * 4, 'CONTACT BOOK', '----' * 4)
contact_list = {}
while True:
    print('''
    1 --> View contacts
    2 --> Add a contact
    3 --> Delete a contact
    4 --> Edit a contact
    5 --> Exit
    ''')
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 5:
        print("Goodbye!")
        break
    elif choice == 1:
        if not contact_list:
            print("No contacts found. Please add some contacts first.")
        else:
            print("\nYour contacts:")
            for name, number in contact_list.items():
                print(f"   {name}: {number}")
    elif choice == 2:
        name = input("Enter name: ").strip()
        if not name:
            print(" Name cannot be empty.")
            continue
        try:
            number = int(input("Enter phone number: "))
        except ValueError:
            print("Invalid number. Please enter digits only.")
            continue
        contact_list[name] = number
        print(f"Added: {name} → {number}")
    elif choice == 3:
        name = input("Enter the name of the contact to delete: ").strip()
        if name in contact_list:
            del contact_list[name]
            print(f"Deleted {name}")
        else:
            print(f"'{name}' not found in contacts.")
    elif choice == 4:
        name = input("Enter the name of the contact to edit: ").strip()
        if name in contact_list:
            try:
                new_number = int(input(f"Enter new number for {name}: "))
            except ValueError:
                print("Invalid number.")
                continue
            contact_list[name] = new_number
            print(f"Updated {name} → {new_number}")
        else:
            print(f"'{name}' not found.")

    else:
        print("Invalid choice. Please select 1-5.")