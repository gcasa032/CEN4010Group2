from flask import Flask, render_template, url_for, Response, request
from flask_mysqldb import MySQL

from classes.book import Book
from classes.author import Author
from classes.user import User
from classes.rating import Rating
from classes.booksearch import BookSearch
from classes.booklist import BookList
from classes.rater import Rater

import MySQLdb.cursors
import datetime

app = Flask(__name__)

app.secret_key = 'admin'

# Database connection details
app.config['MYSQL_HOST'] = 'geektext.co6gooerckmv.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'TXwUJ8cGvDXjdVVPXSsl'
app.config['MYSQL_DB'] = 'geektextdb'

# initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def hello():
    # Renders the "index.html" file, linking to individual feature demos
    return render_template('index.html')


@app.route('/feature1', methods=['GET'])
def feature1():

    #Search by genre "Horror" and "Fantasy"
    search = BookSearch(mysql)
    horror = search.bookByGenre("Horror")
    fantasy = search.bookByGenre("Fantasy")
    byRating = search.bookByRating(3)
    topSellers = search.giveTopSellers()

    #Create BookList object
    alist = BookList(search.giveTopSellers())
    getX = alist.returnxbooks(3)
    getY = alist.returnxbooks(2)


    #renders the feature1.htmls file and passes horror and fantasy lists containing books of that genre
    return render_template("feature1.html", horror=horror, fantasy=fantasy, topSellers=topSellers, byRating=byRating, getX=getX, getY=getY)

@app.route('/feature2')
def feature2():
    return "Feature 2"

@app.route('/feature3')
def feature3():
    return "Feature 3"

@app.route('/feature4')
def feature4():
    return "Feature 4"

@app.route('/feature5', methods=['POST', 'GET'])
def feature5():

    rater = Rater(mysql)

    if request.method == "POST":

        newRating = []
        #not getting any data from here
        newRating.append(request.form['isbn'])
        newRating.append(request.form['userId'])
        newRating.append(request.form['rating'])
        newRating.append(request.form['comment'])
        newRating.append(datetime.date.today())

        rating = Rating(newRating)

        rater.createRating(rating)

    allOpinions = rater.displayOpinion()
    allOrderOpinions = rater.orderReviews()

    return render_template("feature5.html",allOpinions = allOpinions, allOrderOpinions = allOrderOpinions)

@app.route('/newReview', methods=['POST', 'GET'])
def newReview():

    return render_template("newReview.html")

@app.route('/feature6')
def feature6():
    return "Feature 6"


if __name__ == '__main__':
    app.run(debug=True)
