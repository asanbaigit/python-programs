import datetime
class Author:
    def __init__(self,id,n,dob,dod,books):
        self.id = id
        self.name = n
        self.dob = dob
        self.dod = dod
        self.books = books

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.dob + ' ' + self.dod + ' ' + self.books

