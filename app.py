from flask import Flask, render_template, url_for, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors
from classes.book import Book
from classes.author import Author
from classes.bookSearch import bookSearch


app = Flask(__name__)

app.secret_key = 'admin'

# Database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
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
    search = bookSearch(mysql)
    horror = search.bookByGenre("Horror")
    fantasy = search.bookByGenre("Fantasy")
    topSellers = search.giveTopSellers()

    #renders the feature1.htmls file and passes horror and fantasy lists containing books of that genre
    return render_template("feature1.html", horror=horror, fantasy=fantasy, topSellers=topSellers)

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
    return "Feature 5"

@app.route('/feature6')
def feature6():
    return "Feature 6"


if __name__ == '__main__':
    app.run()
