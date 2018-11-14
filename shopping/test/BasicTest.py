import sys
import traceback
from shopping.business import business

def runTest1():
    products = business.getProducts()
    for product in products:
        print("Product: " + product.name)

def main():
    try:
        business.open()
        runTest1()
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
