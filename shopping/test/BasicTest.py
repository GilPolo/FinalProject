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
    print(str(product))

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
    print("Saving Cart...")
    cart.saveCart()
    product = db.get_product(1)
    print(str(product))

def main(argv):
    try:
        business.open()
        Test1()
        Test2()
        Test3()
    except Exception as e:
        print >>sys.stderr, "Exception Occurred: %s" % e
        print >>sys.stderr, traceback.print_exc()
    except:
        print >>sys.stderr, "Unexpected Exception Occurred"
        print >>sys.stderr, traceback.print_exc()
    finally:
        business.close()

if __name__ == "__main__":
    main( sys.argv )
