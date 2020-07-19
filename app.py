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
app.config['MYSQL_PASSWORD'] = '}2H4tktY%'
app.config['MYSQL_DB'] = 'geektextdb'

# initialize MySQL
mysql = MySQL(app)

@app.route('/')
def hello():
    
    return render_template('index.html')


@app.route('/feature1', methods=['GET'])
def feature1():

    #Search by genre "Horror"
    search = bookSearch(mysql)
    horror = search.bookByGenre("Horror")
    fantasy = search.bookByGenre("Fantasy")

    return render_template("feature1.html", horror=horror, fantasy=fantasy)

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