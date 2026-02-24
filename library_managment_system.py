books = ["Basic Electrical Engineering", 
         "Basic Engineering Drawing", 
         "Applied Physics", 
         "Mathematics"]

borrowed_books = []

while True:
    print("\n===== Library Menu =====")
    print("1 --> View available books")
    print("2 --> Borrow a book")
    print("3 --> Return a book")
    print("4 --> Exit")

    try:
        choice = int(input("Choose a valid option [1-4]: "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    if choice == 4:
        print("Thanks for choosing us. Bye!")
        break

    elif choice == 1:
        if books:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)
        else:
            print("No books available right now.")

    elif choice == 2:
        borrow_book_name = input("Enter the book name: ").strip()

        if borrow_book_name in books:
            books.remove(borrow_book_name)
            borrowed_books.append(borrow_book_name)
            print(f"You have borrowed '{borrow_book_name}'. Please return it after reading.")
        else:
            print("Sorry, that book is not available.")

    elif choice == 3:
        return_book_name = input("Enter the book name to return: ").strip()

        if return_book_name in borrowed_books:
            borrowed_books.remove(return_book_name)
            books.append(return_book_name)
            print(f"You have successfully returned '{return_book_name}'.")
        else:
            print("This book was not borrowed from this library.")

    else:
        print("Invalid option! Please choose between 1 and 4.")