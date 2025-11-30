# book.py
# Demonstrates Encapsulation + Inheritance + Polymorphism

class Book:
    def _init_(self, title, author, price):
        # Encapsulation (private attributes)
        self.__title = title
        self.__author = author
        self.__price = price

    # Getter & Setter for Title
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # Getter & Setter for Author
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    # Getter & Setter for Price
    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive.")

    # Polymorphic method
    def book_info(self):
        return f"Book: {self._title} by {self.author}, Price: ₹{self._price}"


# INHERITANCE: Child class
class EBook(Book):
    def _init_(self, title, author, price, file_size):
        super()._init_(title, author, price)
        self.__file_size = file_size  # MB

    # Polymorphism: override book_info()
    def book_info(self):
        return f"E-Book: {self.get_title()} ({self.__file_size}MB), Price: ₹{self.get_price()}"


class PrintedBook(Book):
    def _init_(self, title, author, price, pages):
        super()._init_(title, author, price)
        self.__pages = pages

    # Polymorphism: override book_info()
    def book_info(self):
        return f"Printed Book: {self.get_title()} – {self.__pages} pages, Price: ₹{self.get_price()}"
