from flask import Flask, render_template, url_for, Response, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
from classes.book import Book
from classes.author import Author
from classes.user import User
from classes.rating import Rating

from classes.booksearch import BookSearch
from classes.booklist import BookList
from classes.rater import Rater
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


@app.errorhandler(404)
def notfound(e):
    return render_template('404.html')


@app.route('/feature4')
def feature4():
    return render_template('feature4.html')


@app.route('/books')
def book_list():
    authors = Author.query.all()
    books = {}
    for author in authors:
        book = Book.query.filter(Book.idAuthor == author.idAuthor).all()
        if len(book):
            books[author.idAuthor] = book
    return render_template("booklist.html", books=books, authors=authors)


@app.route('/books/new/', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        author_name = request.form['author'].split(' ')
        author = Author.query.filter(Author.firstName == author_name[0] and Author.lastName == author_name[1]).all()
        print(author)
        if author:
            new_book = Book(isbn=request.form.get('isbn'),
                            bookName=request.form.get('name'),
                            idAuthor=author[0].idAuthor,
                            description=request.form.get('description'),
                            price=request.form.get('price'),
                            publisher=request.form.get('publisher'),
                            yearPublished=request.form.get('yearPublished'),
                            copiesSold=request.form.get('copiesSold'),
                            genre=request.form.get('genre'))
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('book_list'))
        else:
            flash("author not found")
            return render_template('newbook.html')

    if request.method == 'GET':
        return render_template('newbook.html')


@app.route('/author/new/', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        newAuthor = Author(firstName=request.form.get('firstName'),
                           lastName=request.form.get('lastName'),
                           biography=request.form.get('biography'),
                           publisher=request.form.get('publisher'))
        db.session.add(newAuthor)
        db.session.commit()
        return redirect(url_for('book_list'))
    if request.method == 'GET':
        return render_template('newauthor.html')


@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')


@app.route('/delete_author/<int:idAuthor>', methods=['POST', 'GET'])
def delete_author(idAuthor):
    books = Book.query.filter(Book.idAuthor == idAuthor).all()
    if books:
        for book in books:
            db.session.delete(book)
        db.session.commit()
    author = Author.query.get(idAuthor)
    if author:
        db.session.delete(author)
        db.session.commit()
    return redirect(url_for('book_list'))


@app.route('/delete_book/<int:isbn>', methods=['POST', 'GET'])
def delete_book(isbn):
    book = Book.query.filter(Book.isbn == isbn).first()
    if book:
        print(book.bookName, "test")
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('book_list'))


@app.route('/author_detail/<int:idAuthor>', methods=['GET'])
def author_detail(idAuthor):
    author = Author.query.filter(Author.idAuthor == idAuthor).first()
    return render_template('authordetail.html', author=author)


@app.route('/book_detail/<int:isbn>', methods=['GET'])
def book_detail(isbn):
    book = Book.query.filter(Book.isbn == isbn).first()
    author = Author.query.filter(Author.idAuthor == book.idAuthor).first()
    return render_template('bookdetail.html', book=book, author=author)


@app.route('/search_book/', methods=['POST'])
def search_book():
    isbn = int(request.form.get('isbn').strip())
    book = Book.query.filter(Book.isbn == isbn).first()
    if book:
        author = Author.query.filter(Author.idAuthor == book.idAuthor).first()
        return render_template('bookdetail.html', book=book, author=author)
    else:
        return render_template('search.html')


@app.route('/search_author/', methods=['POST'])
def search_author():
    fullname = request.form.get('author').strip().split(' ')
    authors = Author.query.filter(Author.firstName == fullname[0] and Author.lastName == fullname[1])
    books = {}
    for author in authors:
        book = Book.query.filter(Book.idAuthor == author.idAuthor).all()
        if len(book):
            books[author.idAuthor] = book
    return render_template("booklist.html", books=books, authors=authors)


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
    averageRating = rater.calcAvgR('1443434973')
    

    return render_template("feature5.html",allOpinions = allOpinions, allOrderOpinions = allOrderOpinions, averageRating=averageRating)

@app.route('/newReview', methods=['POST', 'GET'])
def newReview():

    return render_template("newReview.html")

@app.route('/feature6')
def feature6():
    return "Feature 6"


if __name__ == '__main__':
    app.run(debug=True)
