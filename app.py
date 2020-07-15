from flask import Flask, render_template, url_for, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors

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
    cur = mysql.connection.cursor()
    resultsValue = cur.execute("SELECT * FROM book")
    if resultsValue > 0:
        vidDetails = cur.fetchall()
        return vidDetails[0][2]

    return "ERROR: No data was found"

if __name__ == '__main__':
    app.run()