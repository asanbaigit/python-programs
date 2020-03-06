class Book:
    def __init__(self,title,author,summary,imprint,ISBN,genre,language):
        self.title = title
        self.author = author
        self.summary = summary
        self.imprint = imprint
        self.ISBN = ISBN
        self.genre = genre
        self.language = language

    def __str__(self):
        return self.title + ' ' + self.author.name + ' ' + self.summary + ' '+ self.imprint + ' '+ self.ISBN+' ' + self.genre.name + ' ' + self.language.name

        