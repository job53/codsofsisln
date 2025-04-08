import sqlite3
import hashlib
from sqlite3 import Error

class DataBaseManager():
    '''
    Class
    '''
    database = r"./goldpoints.db"

    def create_connection(self):
        '''
        create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        '''
        conn = None
        try:
            conn = sqlite3.connect(self.database)
        except Error as e:
            print(e)

        return conn


    def create_user(self, conn, user):
        try:
            sql = '''INSERT INTO
            users (companyId, nickname, email, token, firstName, lastName, rfc, points, utype, created)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cur = conn.cursor()
            cur.execute(sql, user)
            conn.commit()
            msg = "Registered Successfully"
        except:
            conn.rollback()
            msg = "Error occured"
        return msg

    def create_product(self, conn, product):
        '''
        Create a new task
        :param conn:
        :param product:
        :return:
        '''

        sql = '''
        INSERT INTO "product" ("id","name","family","unit","cost","cost_150","cost_250","cost_500")
        VALUES(?,?,?,?,?,?,?,?)
        '''
        cur = conn.cursor()
        cur.execute(sql, product)
        return cur.lastrowid

    def is_an_existing_product(self, conn, code):
        '''
        Query if exist a role in the table
        :param conn:
        :param code:
        :param role_name:
        :return:
        '''
        sql = '''SELECT * FROM product WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (code,))

        rows = cur.fetchall()

        if len(rows) > 0 :
            return True

        return False

    def update_product(self, conn, product):
        '''
        Create a new task
        :param conn:
        :param user:
        :return:
        '''

        sql = '''
        UPDATE "product"
        SET name = ?,
            family = ?,
            unit = ?,
            cost = ?,
            cost_150 = ?,
            cost_250 = ?,
            cost_500 = ?
        WHERE
            id = ?;
        '''
        cur = conn.cursor()
        cur.execute(sql, product)
        return cur.lastrowid

    def get_products(self, conn):
        '''
        Query if exist a role in the table
        :param conn:
        :param role_name:
        :return:
        '''
        sql = '''SELECT * FROM products'''
        cur = conn.cursor()
        cur.execute(sql, ())

        rows = cur.fetchall()

        return rows

    def get_login_details(self, conn, session):
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            firstName = ''
            noOfItems = 0
        else:
            loggedIn = True
            sql_user = '''SELECT userId, firstName FROM users WHERE email = ?'''
            cur.execute(sql_user, (session['email'],))
            userId, firstName = cur.fetchone()
            sql_kart = '''SELECT count(productId) FROM kart WHERE userId = ?'''
            cur.execute(sql_kart, (str(userId),))
            noOfItems = cur.fetchone()[0]

        return (loggedIn, firstName, noOfItems)

    def is_valid(self, conn, nickname, token):
        etoken = hashlib.md5(token.encode()).hexdigest()
        cur = conn.cursor()
        sql = '''SELECT * FROM users WHERE nickname = ? AND token = ?'''
        cur.execute(sql, (nickname, etoken,))
        data = cur.fetchall()
        for row in data:
            return row
        return False

    def getFamilies(self, conn):
        cur = conn.cursor()
        sql = '''SELECT * FROM families'''
        cur.execute(sql, ())
        data = cur.fetchall()
        if data:
            return data
        return False

    def getCompanies(self, conn):
        cur = conn.cursor()
        sql = '''SELECT companyId, name FROM companies'''
        cur.execute(sql, ())
        data = cur.fetchall()
        if data:
            return data
        return False

    def get_cart_list(self, conn, userId):
        cur = conn.cursor()
        sql_cart = '''SELECT *  FROM products, karts
        WHERE products.productId = karts.productId AND karts.userId = ?'''
        cur.execute(sql_cart, (userId))
        products = cur.fetchall()

        return products

    def add_to_cart(self, conn, userId, productId, quantity):
        cur = conn.cursor()
        try:
            sql_check_product= '''SELECT * FROM karts WHERE userId = ? AND productId = ? '''
            cur.execute(sql_check_product, (userId, productId))
            msg = cur.fetchone()
            # check if it is empty and print error
            if msg:
                if int(quantity) == 1:
                    quantity = msg[2] + 1
                sql_cart = '''UPDATE karts SET quantity = ?
                WHERE userId = ? AND productId = ?
                '''
                cur.execute(sql_cart, (quantity, userId, productId))
            else:
                sql_cart = '''INSERT INTO karts (userId, productId, quantity)
                VALUES (?, ?, ?)
                '''
                cur.execute(sql_cart, (userId, productId, quantity))
            conn.commit()
            msg = "Added successfully"
        except Exception as e:
            print(e)
            conn.rollback()
            msg = "Error occurred"
        return msg

    def remove_from_cart(self, conn, userId, productId):
        try:
            cur = conn.cursor()
            sql_cart = '''DELETE FROM karts WHERE userId = ? AND productId = ? '''
            cur.execute(sql_cart, (userId, productId))
            conn.commit()
            msg = "removed successfully"
        except Exception as e:
            conn.rollback()
            msg = "error occurred"

        return msg

    def clean_user_cart(self, conn, userId):
        try:
            cur = conn.cursor()
            sql_cart = '''DELETE FROM karts WHERE userId = ? '''
            cur.execute(sql_cart, (userId))
            conn.commit()
            msg = "cleaned successfully"
        except Exception as e:
            conn.rollback()
            msg = "error occurred"

        return msg

    def checkout(self, conn, email):
        cur = conn.cursor()
        sql_user = '''SELECT userId FROM users WHERE email =?'''
        cur.execute(sql_user, (email,))
        userId = cur.fetchone()[0]
        sql_cart = '''SELECT product.id, product.name, product.cost, product.unit FROM product, kart
        WHERE product.id = kart.productId AND kart.userId =?'''
        cur.execute(sql_cart, (str(userId),))
        products = cur.fetchall()
        totalPrice = 0
        for row in products:
            totalPrice += row[2]
            print(row)
            sql_order = '''INSERT INTO orders (userId, productId) VALUES (?, ?)'''
            cur.execute(sql_order, (userId, row[0],))
        sql_del_cart = '''DELETE FROM kart WHERE userId =?'''
        cur.execute(sql_del_cart, (str(userId),))
        conn.commit()

        return products, totalPrice