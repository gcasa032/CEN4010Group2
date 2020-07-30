from classes.book import Book
from flask_mysqldb import MySQL

# AUTHOR: Guillermo Casal

class BookSearch:

    def __init__(self, mysql: MySQL):
        #bookSearch object must be initiated with a mysql object to run querys
        self.mysql = mysql
         
    """
        Given a string containing a book genre, this method
        returns a list of Book objects who have the genre given in the paramater         
    """    
    def bookByGenre(self, genre: str) -> list:

        bookList = []
        queryStr = "SELECT * FROM book WHERE genre =  '" + genre + "'"

        cur = self.mysql.connection.cursor()
        cur.execute(queryStr)

        queryResult = cur.fetchone()

                # loop through results of query 
        while queryResult is not None:
            # Each result becomes a Book object and is added to list
            bookList.append(Book(queryResult))
            queryResult = cur.fetchone()
        return bookList


    def giveTopSellers(self) -> list:

        bookList = []
        queryStr = "SELECT * FROM book ORDER BY copiesSold DESC LIMIT 10"
        

        cur = self.mysql.connection.cursor()
        cur.execute(queryStr)

        queryResult = cur.fetchone()

        # loop through results of query 
        while queryResult is not None:
            # Each result becomes a Book object and is added to list
            bookList.append(Book(queryResult))
            queryResult = cur.fetchone()
        return bookList


    def bookByRating(self, rating: int) -> list:
        
        bookList = []
        queryStr = "SELECT book.*, rating.rating FROM book INNER JOIN rating on book.isbn = rating.book_isbn WHERE rating >= " + str(rating)
        cur = self.mysql.connection.cursor()
        cur.execute(queryStr)

        queryResult = cur.fetchone()

        # loop through results of query 
        while queryResult is not None:
            # Each result becomes a Book object and is added to list
            book = Book(queryResult)
            book.setRating(queryResult[9])
            bookList.append(book)
            queryResult = cur.fetchone()
        return bookList

