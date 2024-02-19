class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for book_line in book_lines:
            book_info = book_line.split(',')
            book_title, book_author, release_date, num_pages = book_info
            print(f"Title: {book_title}, Author: {book_author}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        self.file.seek(0)
        info = self.file.read().splitlines()
        while True:
            remove = input("Enter the book name to remove: ")
            self.file.seek(0)
            temp = []
            for i in info:
                title = (i.split(','))

                temp.append(title)
                print(temp)
            if remove not in temp:
                print("That book does not exist! Try Again:")


            else:
                self.file.seek(0)
                self.file.truncate()
                self.file.write('\n'.join(temp))
                print("Book removed successfully.")
                break




iskenderiye = Library()

while True:
    print("\n MENU ")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        iskenderiye.list_books()
    elif choice == "2":
        iskenderiye.add_book()
    elif choice == "3":
        iskenderiye.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
