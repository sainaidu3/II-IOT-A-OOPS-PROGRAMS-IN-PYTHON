class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    def __str__(self):
        status = "Availble" if self.is_availble else "Not Available"
        return f"{self.title} by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"'{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"'{title}' removed from the library.")
                return
      print(f"'{title}'removed from the library.")
      return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.is_available:
            book.is_available:
              book.is_available = False
              print(f"'borrwed '{book.title}'.")
        elif book:
            print(f"'{book.title}' is already borrower.")

     def return_book(self, title):
         book = self.search_book(title)
         if book and not book.is_available:
             book.is_available = True
             print(f"You returned '{book.title)'.")
        elif book:
            print(f"'{book.title}'was not borrowed.")
            
lib = Library()
lib.add_book(Book{"Python Basics", "SAI NAIDU"))
lib.add_
