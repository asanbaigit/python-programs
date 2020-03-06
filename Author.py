#import datetime
class Author:
    def __init__(self,n,dob,dod):
        self.name = n
        self.dob = dob
        self.dod = dod
        self.books = []

    def add_book(self,book):
        self.books.append(book)
  
    def __str__(self):
        b = [book.title for book in self.books]
        return self.name + ": " + ", ".join(b) + ' ' + self.dob +' '+ self.dod