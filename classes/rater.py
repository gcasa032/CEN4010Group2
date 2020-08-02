#AUTHOR: STEPHAN BELIZAIRE
from classes.rating import Rating
from flask_mysqldb import MySQL
import datetime

class Rater:

    def __init__(self, mysql: MySQL):

        self.mysql = mysql

    #Display all review/ratings
    def displayOpinion(self):

        #The cursor comunicates with the database to run querys
        cur = self.mysql.connection.cursor()
        reviewList = []
        query = "SELECT * FROM rating ORDER BY rating ASC"
        # execute the query
        cur.execute(query)
        allReviews = cur.fetchone()
        while allReviews is not None:
            # Each result becomes a new Rating and is added to the list
            reviewList.append(Rating(allReviews))
            allReviews = cur.fetchone()
        return reviewList

    #Create a new review
    def createRating(self, newRating: Rating):

        cur = self.mysql.connection.cursor()

        cur.execute("INSERT INTO `geektextdb`.`rating` (`book_isbn`,`user_iduser`,`rating`,`comment`,`date`) VALUES (%s,%s,%s,%s,%s)",(newRating.book_isbn, newRating.user_iduser, newRating.rating, newRating.comment, str(newRating.date)))

        self.mysql.connection.commit()

    #Order the review from descending order
    def orderReviews(self):

        cur = self.mysql.connection.cursor()

        allRated = []
        query = "SELECT * FROM rating ORDER BY rating DESC"
        cur.execute(query)
        allRatings = cur.fetchone()
        while allRatings is not None:
            allRated.append(Rating(allRatings))
            allRatings = cur.fetchone()
        return allRated

    #calculate the average of all the total ratings
    def calcAvgR(self, isbn: str):
        cur = self.mysql.connection.cursor()

        allRated = []
        query = "SELECT avg(rating) FROM geektextdb.rating WHERE book_isbn = '" + isbn + "'"
        # Should be avg rating of a particualr book not all books
        cur.execute(query)
        avgRating = cur.fetchone()
        return str(avgRating[0])
