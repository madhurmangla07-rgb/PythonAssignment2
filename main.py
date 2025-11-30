# main.py
from book import Book, EBook, PrintedBook
from inventory import Inventory


def main():
    inventory = Inventory()

    while True:
        print("\n===== BOOK INVENTORY MENU =====")
        print("1. Add Printed Book")
        print("2. Add E-Book")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            price = float(input("Price: "))
            pages = int(input("Pages: "))
            book = PrintedBook(title, author, price, pages)
            inventory.add_book(book)

        elif choice == "2":
            title = input("Title: ")
            author = input("Author: ")
            price = float(input("Price: "))
            size = float(input("File size (MB): "))
            book = EBook(title, author, price, size)
            inventory.add_book(book)

        elif choice == "3":
            title = input("Enter title to search: ")
            book = inventory.search_book(title)
            if book:
                print(book.book_info())
            else:
                print("Book not found.")

        elif choice == "4":
            title = input("Enter title to remove: ")
            inventory.remove_book(title)

        elif choice == "5":
            inventory.display_inventory()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if _name_ == "_main_":
    main()
