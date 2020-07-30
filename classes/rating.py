#AUTHOR Stephan Belizaire

class Rating:

    def __init__(self, newRating: list):

        self.book_isbn = newRating[0]
        self.user_iduser = newRating[1]
        self.rating = newRating[2]
        self.comment = newRating[3]
        self.date = newRating[4]
