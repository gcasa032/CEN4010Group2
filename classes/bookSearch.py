from classes.book import Book
from flask_mysqldb import MySQL

class bookSearch():

    def __init__(self, mysql: MySQL):
        self.mysql = mysql
        
    def bookByGenre(self) -> Book:
        cur = self.mysql.connection.cursor()
        resultsValue = cur.execute("SELECT * FROM book")
        if resultsValue > 0:
            vidDetails = cur.fetchone()
            newBook = Book(vidDetails)
            return newBook
        return None
