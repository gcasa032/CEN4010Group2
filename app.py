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
app.config['MYSQL_PASSWORD'] = ':1aduhTrr-'
app.config['MYSQL_DB'] = 'geektextdb'

# initialize MySQL
mysql = MySQL(app)

@app.route('/')
def hello():
    test = bookSearch(mysql)
    book = test.bookByGenre()
    return book.bookName


if __name__ == '__main__':
    app.run()