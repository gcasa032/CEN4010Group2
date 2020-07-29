#AUTHOR: STEPHAN BELIZAIRE
from classes.rating import Rating
from flask_mysqldb import MySQL
from classes.user import User

class Rater:

    def __init__(self, mysql: MySQL, user: User, rating: rating):

        self.mysql = mysql
        self.user = user
        self.rating = rating

        #Display all review/ratings

    def displayOpinion():

        #The cursor comunicates with the database to run querys
        cur = self.mysql.connection.cursor()
        reviewList = []
        query = "SELECT * FROM rating"
        # execute the query
        cur.execute(query)
        allReviews = cur.fetchall()
        reviewList.append(Rating(allReviews))
        return reviewList

            #Create a new review
    def createOpinion(text1,text2,text3,text4,text5):

        cur = self.mysql.connection.cursor()
        nRating = Rating(text1,text2,text3,text4,text5)
        self.session.add(nRating)
        self.session.commit()

            #Order the review from descending order
    def orderReviews():

        cur = self.mysql.connection.cursor()

        allRated[]
        query = "SELECT * FROM geektextdb.rating ORDER BY rating DESC"
        cur.execute(query)
        allRatings = cur.fetchall()
        allRated.append(Rating(allReviews))
        return allRated

            #calculate the average of all the total ratings
    def calcAvgR():
        cur = self.mysql.connection.cursor()

        allRated[]
        query = "SELECT * FROM geektextdb.rating ORDER BY rating"
        cur.execute(query)
        allRatings = cur.fetchall()
        allRated.append(Rating(allReviews))
        for x in allRating:
            total += x
            return total
        return total
