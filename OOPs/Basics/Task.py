# Make a simple Book class with attributes like book_isbn, book_name, book_author_name, book_price. Make another class called Library and inherit Book class then use the attributes of book in the library class. use array of objects in library class then use the methods of book class (showBookDetails()) and use them.

class Book:
    def __init__(self, book_isbn: int, book_name: str, book_author_name: str, book_price: float) -> None:
        self.book_isbn = book_isbn
        self.book_name = book_name
        self.book_author_name = book_author_name
        self.book_price = book_price

    def showBookDetails(self):
        print(f"Book ISBN: {self.book_isbn}")
        print(f"Book Name: {self.book_name}")
        print(f"Book Author Name: {self.book_author_name}")
        print(f"Book Price: {self.book_price}")

class Library (Book):
    def __init__(self, isbn, name, author_name, price) -> None:
        super().__init__(isbn, name, author_name, price)
    
    def getBookDetails(self):
        print("---------------------------------")
        super().showBookDetails()
    
if __name__ == "__main__":
    library = []
    library.append(Library(124, "Python", "Arin Pra", 230.3))
    library.append(Library(345, "Java", "Dhairya", 450.99))
    library.append(Library(333, "C", "Vishva", 556.66))
    library.append(Library(678, "CPP", "Fatma", 999.99))

    for i in library:
        i.getBookDetails()