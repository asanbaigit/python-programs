from Language import Language
from Genre import Genre
from Author import Author
from Book import Book
#from bookinstance import BookInstance
#import datetime
genres = []
langs = []
authors = []
books = []

# create genre and add it to genres
genre = Genre("Roman")
genres.append(genre)

# create a language and add it to langs
lang = Language("Kyrgyz")
langs.append(lang)

# create an author and add to authors list
author1 = Author("Chyngyz Aitmatov", "1940", "2008")
author2 = Author("Alykul Osmonov", "1900", "1970")
authors.append(author1)
authors.append(author2)

# create books with already created author, genre and language
book1 = Book("Ak Keme", author1,'Nurgazy jonundo roman','Basmakana','123456789', genre, lang)
book2 = Book("Ata Jurt",author2,'Patriottuk yr','Basmakana','124356789',  genre, lang)

# add created books to the books list
books.append(book1)
books.append(book2)

# add created books to their author
author1.add_book(book1)
author2.add_book(book2)

print("1.List all books\n2.List all authors\n3.Add a new book\n4.Remove a book\n0.Exit\n")
choice = int(input("Enter your choice: "))

while choice != 0:   
    if choice == 1:
        # print(", ".join([book.title for book in books]))
        print()
        print("Book name: Author -Summary-imprint-ISBN- Genre - Language")
        for book in books:
            print(book)
        print()
    elif choice == 2:
        # print(", ".join([author.name for author in authors]))
        for author in authors:
            print(author)
        print()
    elif choice == 3:
        title = input("Enter book title: ")
        genre_name = input("Enter book genre: ")
        lang_name = input("Enter language: ")
        summary = input("Enter the summary: ")
        imprint = input("Enter the imprint: ")
        ISBN = input("Enter the ISNB: ")

        for author in authors:
            print(str(authors.index(author)) + ". " + author.name)
        print(str(len(authors)) + ". Add new author")
        choice = int(input("Choose from the options above: "))
        if choice == len(authors):
            name = input("Name: ")
            dob = input("DOB: ")
            dod = input("DOD: ")
            new_author = Author(name, dob, dod)

            genre = Genre(genre_name)
            genres.append(genre)
            
            lang = Language(lang_name)
            langs.append(lang)
            
            new_book = Book(title, new_author,summary,imprint,ISBN,genre, lang)
            new_author.add_book(new_book)
            authors.append(new_author)
            books.append(new_book)
            print("Book successfully added.")

    print("1.List all books\n2.List all authors\n3.Add a new book\n4.Remove a book\n0.Exit\n")
    choice = int(input("Enter your choice: "))
