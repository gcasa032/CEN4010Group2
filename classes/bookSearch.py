from classes.book import Book
from flask_mysqldb import MySQL

# AUTHOR: Guillermo Casal

class bookSearch():

    def __init__(self, mysql: MySQL):
        #bookSearch object must be initiated with a mysql object to run querys
        self.mysql = mysql
        

    """
        Given a string containing a book genre, this method
        returns a list of Book objects who have the genre given in the paramater         
    """    
    def bookByGenre(self, genre: str) -> list:

        #The cursor comunicates with the database to run querys
        cur = self.mysql.connection.cursor()

        bookList = []
        query = "SELECT * FROM book WHERE genre =  '" + genre + "'"

        # execute the query
        cur.execute(query)

        
        queryResult = cur.fetchone()
        # loop through results of query 
        while queryResult is not None:
            # Each result becomes a Book object and is added to list
            bookList.append(Book(queryResult))
            queryResult = cur.fetchone()
        return bookList

