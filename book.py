choice = 1
while choice != 4:
    print('====== Welcome to the Library ======\n')
    print('         Please choose a option:')
    print('         1. List all the books')
    print('         2. Request a book')   
    print('         3. Return a Book')
    print('         4. Exit the Library\n\n')      

    choice = int(input('Enter a Choice: '))

    if choice == 1:
        print('Books present in the library are: ')
        print('*Algorithms\n*Django\n*C++\n*Python\n*C\n*HTML and CSS\n')
    elif choice == 2:
        book_name = input('Enter the name of the book you want to borrow: ')
        print('You have been issued ' + book_name + '. Please keep it safe and return it within 30 days ')
    elif choice == 3:
        book_name = input('Enter the name of the book you want to return: ')
        print('Thanks for returning this book! Hope you enjoyed reading it. Have a great dayahead! ')
    else:
        print('Thank you for using Library. Happy reading! Have great day ahead!')

