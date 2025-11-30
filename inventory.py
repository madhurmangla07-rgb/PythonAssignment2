# inventory.py
# Demonstrates Encapsulation & collection management

class Inventory:
    def _init_(self):
        self.__books = []     # Encapsulated list of books

    def add_book(self, book):
        self.__books.append(book)
        print("Book added successfully.")

    def remove_book(self, title):
        for book in self.__books:
            if book.get_title().lower() == title.lower():
                self.__books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.__books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def display_inventory(self):
        if not self.__books:
            print("Inventory is empty.")
        else:
            print("\n--- Book Inventory ---")
            for book in self.__books:
                print(book.book_info())
