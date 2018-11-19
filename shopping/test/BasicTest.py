import sys
import traceback
from ..business import business
from ..db import db

def Test1():
    print("Running: Test1....")
    products = business.getProducts()
    for product in products:
        print("Product: " + product.name)

def Test2():
    print()
    print("Running: Test2....")
    product = db.get_product(1)

def Test3():
    print()
    print("Running: Test3....")
    print("Creating Order....")
    cart = business.Cart()
    product1 = db.get_product(1)
    product2 = db.get_product(2)
    product3 = db.get_product(3)
    lineItem = business.LineItem(0, 1, product1, 2)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 2, product2, 3)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 3, product3, 1)
    cart.addItem(lineItem)
    print("Cart Total {:9.2f}".format(cart.getTotal()))
    print("Creating Cart...")
    cart.createCart(status=1)
    print("Cart order id created= ", cart.orderID)

def Test4():
    print()
    print("Running: Test4....")
    print("Creating Order....")
    cart = business.Cart()
    product1 = db.get_product(1)
    product2 = db.get_product(2)
    product3 = db.get_product(3)
    product4 = db.get_product(4)
    lineItem = business.LineItem(0, 1, product1, 2)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 2, product2, 3)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 3, product3, 1)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 4, product4, 4)
    cart.addItem(lineItem)
    cart.removeItem(1)
    print("Cart Total {:9.2f}".format(cart.getTotal()))
    print("Saving Cart...")
    cart.createCart(status=1)
    print("Cart order id created= ", cart.orderID)

def Test5():
    print()
    print("Running: Test5....")
    print("Creating Order....")
    cart = business.Cart()
    product1 = db.get_product(1)
    product2 = db.get_product(2)
    product3 = db.get_product(3)
    product4 = db.get_product(4)
    product5 = db.get_product(5)
    lineItem = business.LineItem(0, 1, product1, 2)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 2, product2, 3)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 3, product3, 1)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 4, product4, 4)
    cart.addItem(lineItem)
    lineItem = business.LineItem(0, 5, product4, 6)
    cart.addItem(lineItem)
    print("Cart Total {:9.2f}".format(cart.getTotal()))
    print("Creating Cart...")
    cart.createCart(status=1)
    print("Cart order id created= ", cart.orderID)
    cart = business.readCart(cart.orderID)
    cart.saveCart()
    print("Cart saved...")
    print("Read saved cart back...")
    cart = business.readCart(cart.orderID)
    print("Cart = ", str(cart))

def main(argv):
    try:
        Test1()
        Test2()
        Test3()
        Test4()
        Test5()
    except Exception as e:
        print >>sys.stderr, "Exception Occurred: %s" % e
        print >>sys.stderr, traceback.print_exc()
    except:
        print >>sys.stderr, "Unexpected Exception Occurred"
        print >>sys.stderr, traceback.print_exc()

if __name__ == "__main__":
    main( sys.argv )
