from flask import Flask, render_template, url_for, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors
from classes.book import Book
from classes.author import Author
from classes.user import User
from classes.rating import Rating

from classes.booksearch import BookSearch
from classes.booklist import BookList
from classes.rater import Rater

app = Flask(__name__)

app.secret_key = 'admin'

# Database connection details
app.config['MYSQL_HOST'] = 'geektext.co6gooerckmv.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'TXwUJ8cGvDXjdVVPXSsl'
app.config['MYSQL_DB'] = 'geektextdb'

# initialize MySQL
mysql = MySQL(app)

@app.route('/')
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

    alist = BookList(search.giveTopSellers())
    horror2 = alist.returnxbooks(3)


    #renders the feature1.htmls file and passes horror and fantasy lists containing books of that genre
    return render_template("feature1.html", horror=horror, fantasy=fantasy, topSellers=topSellers, byRating=byRating, horror2= horror2)

@app.route('/feature2')
def feature2():
    return "Feature 2"

@app.route('/feature3')
def feature3():
    return "Feature 3"

@app.route('/feature4')
def feature4():
    return "Feature 4"

@app.route('/feature5')
def feature5():
    return render_template("feature5.html")

@app.route('/feature6')
def feature6():
    return "Feature 6"


if __name__ == '__main__':
    app.run(debug=True)
