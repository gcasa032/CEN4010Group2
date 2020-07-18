# AUTHOR: Guillermo Casal

class Book:

    def __init__(self, bookDetails: list):
        
        self.isbn = bookDetails[0]
        self.idAuthor = bookDetails[1]
        self.bookName = bookDetails[2]
        self.description = bookDetails[3]
        self.price = bookDetails[4]
        self.genre = bookDetails[5]
        self.publisher = bookDetails[6]

