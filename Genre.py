class Genre:
    def __init__(self,id,n):
        self.name = n 
        self.id = id 

    def __str__(self):
        return str(self.id) + ' ' + self.name

        