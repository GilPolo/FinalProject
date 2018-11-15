import sys
import os
import sqlite3
from contextlib import closing
from shopping.business import business

DB_FILE = "_products.db"

conn=None

def open():
    global conn
    if not conn:
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        path = os.path.join(dir_path, DB_FILE)
        print("DB Directory path ", path)
        conn = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_product(row):
    return business.Product(row["productID"], row["name"], row["price"], row["discount"])

def make_order(row):
    return business.Cart(row["orderID"], row["status"], row["date_added"])

def get_products():
    global conn
    query = '''select * from Products'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    products = []
    for row in results:
        products.append(make_product(row))
    return products

def get_product(productID):
    global conn
    query = '''select * from Products where productID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (productID,))
        result = c.fetchone()
    
    if result != None:
        return make_product(result)
    else:
        return None

def create_order():
    global conn
    query = '''insert into Orders (status, date_added) values (1, datetime('now'))'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()
        return get_order(c.lastrowid)

def create_order(cart):
    global conn
    rowid = -1
    query = '''insert into Orders (status, date_added) values (?, datetime('now'))'''
    with closing(conn.cursor()) as c:
        c.execute(query, (cart.status,))
        conn.commit()
        cart.orderID = rowid = c.lastrowid
    return rowid

def get_order(orderID):
    global conn
    query = '''select orderID, status, date_added as "st [timestamp]" from Orders where orderID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (orderID,))
        result = c.fetchone()

    if result != None:
        return make_order(result)
    else:
        return None

def make_lineitem(row):
    product = make_product(row["productID"])
    lineitem = business.LineItem(row["orderID"], row["lineID"], product, row["quantity"])
    return lineitem

def get_lineitems(orderID):
    global conn
    query = '''select * from LineItems where orderID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (orderID,))
        results = c.fetchall()

    lineitems = []
    for result in results:
        lineitems.append(make_lineitem(result))
    return lineitems

def remove_lineitem(orderID):
    global conn
    query = '''delete from LineItems where orderID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (orderID,))
        conn.commit()

def add_lineitems(LineItems):
    global conn
    query = '''insert into LineItems (orderID, lineID, productID, quantity) values(?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        for lineItem in LineItems:
            c.execute(query, (lineItem.orderID,lineItem.orderID,lineItem.productID,lineItem.quantity))
        conn.commit()
