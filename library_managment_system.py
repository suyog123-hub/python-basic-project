books = ["Basic Electrical Engineering", "Basic Engineering Drawing", "Applied Physics", "Mathematics"]
borrowed_books =[]

while True:
    print("\nMenu:")
    print("1 --> View available books")
    print("2 --> Borrow a book")
    print("3 --> Return a book")
    print("4 --> Exit")

    choice = int(input("Choose a valid option [1-4]: "))
    if choice == 4:
        print("thanks for choosing us bye!")
        exit()

    elif choice == 1:
        print("Available books:")
        for book in books:
            print(book)
        

    elif choice == 2:
        borrow_book_name = input("Enter the name of the book you want to borrow: ")
        if borrow_book_name in books:
            books.remove(borrow_book_name)
            borrowed_books.append(borrow_book_name)
            for i in borrowed_books:
              
                print(f"You have borrowed '{i}'books. Please return it after reading.")
        else:
            print("Sorry, that book is not available or already borrowed.")
           

    elif choice == 3:
        return_book_name = input("Enter the name of the book you want to return: ")
        if return_book_name in borrowed_books:
            borrowed_books.remove(return_book_name)
            books.append(return_book_name)
            print("You have successfully returned ",return_book_name, "to the library.")
          
        else:
            print("This book was not borrowed or does not exist in our records.")

    else:
        print("Invalid option! Please choose a number between 1 and 4.")