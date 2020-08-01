from flask_mysql import flask_mysql
from classes.shoppingcart import shoppingcart

class updateCart:

    def __init__(self, mysql: MySQL):

        cursor = None
	try:
		_quantity = int(request.form['quantity'])
		_code = request.form['code']
		# validate the received values
		if _quantity and _code and request.method == 'POST':
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT * FROM product WHERE code=%s", _code)
			row = cursor.fetchone()


