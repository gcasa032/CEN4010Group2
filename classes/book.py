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
        self.yearPublished = bookDetails[7]
        self.copiesSold = bookDetails[8]
        self.rating = -1
        

    def setRating(self, rating: int):
        self.rating = rating

        
