import sys
import os
import sqlite3
from contextlib import closing
from shopping.business import business

DB_FILE = "_products.db"

class Connection:
    def __init__(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        path = os.path.join(dir_path, DB_FILE)
        print("DB Directory path ", path)
        self.conn = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    @property
    def connection(self):
        return self.conn

def make_product(row):
    return business.Product(row["productID"], row["name"], row["price"], row["discount"])

def make_order(row):
    print(str(row))
    #return business.Cart(row["orderID"], row["status"], row["st [timestamp]"])
    return business.Cart(row[0], row[1], row[2])

def get_products():
    conn = Connection()
    query = '''select * from Products'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    products = []
    for row in results:
        products.append(make_product(row))
    return products

def get_product(productID):
    conn = Connection()
    query = '''select * from Products where productID = ?'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query, (productID,))
        result = c.fetchone()
    
    if result != None:
        return make_product(result)
    else:
        return None

def create_order():
    conn = Connection()
    query = '''insert into Orders (status, date_added) values (1, datetime('now'))'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query)
        conn.connection.commit()
        return get_order(c.lastrowid)

def create_order(cart):
    conn = Connection()
    rowid = -1
    query = '''insert into Orders (status, date_added) values (?, datetime('now'))'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query, (cart.status,))
        conn.connection.commit()
        cart.orderID = rowid = c.lastrowid
    return rowid

def save_order(cart):
    conn = Connection()
    rowid = -1
    query = '''update Orders set status=?, date_added = datetime('now') where orderID=?'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query, (cart.status,cart.orderID))
        conn.connection.commit()
        cart.orderID = rowid = c.lastrowid
    return rowid

def get_order(orderID):
    conn = Connection()
    query = '''select orderID, status, date_added as "st [timestamp]" from Orders where orderID = ?'''
    with closing(conn.connection.cursor()) as c:
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

def get_lineItems(orderID):
    conn = Connection()
    query = '''select * from LineItems where orderID = ?'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query, (orderID,))
        results = c.fetchall()

    lineitems = []
    for result in results:
        lineitems.append(make_lineitem(result))
    return lineitems

def remove_lineitems(orderID):
    conn = Connection()
    query = '''delete from LineItems where orderID = ?'''
    with closing(conn.connection.cursor()) as c:
        c.execute(query, (orderID,))
        conn.connection.commit()

def add_lineitems(LineItems):
    conn = Connection()
    query = '''insert into LineItems (orderID, lineID, productID, quantity) values(?, ?, ?, ?)'''
    with closing(conn.connection.cursor()) as c:
        for lineItem in LineItems:
            c.execute(query, (lineItem.orderID,lineItem.lineID,lineItem.productID,lineItem.quantity))
        conn.connection.commit()
