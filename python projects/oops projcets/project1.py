class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def mark_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    
    def mark_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")
    
class Member:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,book,library):
        if book in self.borrowed_books:
            print(f"{self.name} already borrowed '{book.title}'.")
            return
        
        if library.lend_book(book,self):
            self.borrowed_books.append(book)
        
class Library:
    def __init__(self):
        self.books = []
        self.members = [] 

    def add_book(self,book):
        if book in self.books:
            print(f"{book.title} is alrady in the library.")
        else:
            self.books.append(book)

    def register_member(self,member):
        if member in self.members:
            print(f"{member} alredy has a membership.")
        else:
            self.members.append(member)

    def lend_book(self,book,member):
        if member not in self.members:
            print(f"{member.name} is not registered.")
            return False
        
        if book not in self.books:
            print(f"{book} currently book is not available in the library.")
            return False
        
        if  book.is_borrowed:
            print(f"'{book.title}' is already borrowed.")
            return False 
        
        book.mark_borrowed()
        return True
    
    def recive_book(self,book, member):
        if member not in self.members:
            print(f"{member.name} is not registered.")
            return False
        
        if book not in member.brrowed_books:
            print(f"{member.name} did not borrow '{book.title}'")
        
        if not book.is_borrowed:
            print(f"'{book.title}' is not marked as borrowed.")
            return False
        book.mark_returned()
        member.borrowed_books.remove(book)
        return True
    
    def show_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

            