import sys
import os
import sqlite3
from contextlib import closing
from business import business

DB_FILE = "_products.db"

conn=None

def connect():
    global conn
    if not conn:
        conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_product(row):
    return Product(row["productID"], row["name"], row["price"], row["discount"])

def make_order(row):
    return Cart(row["orderID"], row["status"], row["date_added"])

def get_products():
    query = '''select * from Products'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    products = []
    for row in results:
        products.append(make_product(row))
    return products

def get_product(productID):
    query = '''select * from Products where productID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (productID,))
        result = c.fetchone()
    
    if result <> None:
        return make_product(result)
    else:
        return None

def create_order():
    query = '''insert into Orders (status, date_added) values (0, datetime('now'))'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()
        return get_order(c.lastrowid)

def get_order(orderID):
    query = '''select orderID, status, date_added as "st [timestamp]" from Orders where orderID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (orderID,))
        result = c.fetchone()

    if result <> None:
        return make_order(result)
    else:
        return None

def make_lineitem(row):
    product = make_product(row["productID"])
    lineitem = LineItem(row["orderID"], row["lineID"], product, row["quantity"])
    return lineitem

def get_lineitems(orderID):
    query = '''select * from LineItems where orderID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (orderID,))
        results = c.fetchall()

    lineitems = []
    for result in results
        lineitems.append(make_lineitem(result))
    return lineitems

def remove_lineitem(LineItem):
    query = '''delete from LineItems where orderID = ? and lineID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (orderID, lineID))
        conn.commit()

def add_lineitem(LineItem):
