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
    def createOpinion(text1,text2,text3,text4):

        cur = self.mysql.connection.cursor()
        date = datetime.date.today()
        nRating = Rating(text1,text2,text3,text4,date)

        query = "INSERT INTO"
        self.session.add(nRating)
        self.session.commit()

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
    def calcAvgR(self):
        cur = self.mysql.connection.cursor()

        allRated = []
        query = "SELECT * FROM geektextdb.rating ORDER BY rating"
        cur.execute(query)
        allRatings = cur.fetchall()
        allRated.append(Rating(allRatings))
        for x in allRating:
            total += x
            return total
        return total
