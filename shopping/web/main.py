from flask import Flask, flash, redirect, render_template, request, Response, session, abort
from random import randint
from shopping.business import business

app = Flask(__name__)
app.secret_key="My Apollo Secret Key"

@app.route("/")
def index():
    products = business.getProducts()
    return render_template('products.html', products=products)

@app.route("/addtocart/",methods=['POST'])
def addCart():
    if request.method == 'POST':
        print(request.form)
        productID = request.form['addtocart']
        if 'cart' in session:
            cart = session['cart']
            item = cart.getLineItemByProductID(productID)
            if item != None:
                item.quantity = item.quantity + 1
            else:
                product = business.getProduct(productID)
                lineItem = business.LineItem(0, cart.getItemCount() + 1, product, 1)
                cart.addItem(lineItem)
        else:
            cart = business.Cart()
            product = business.getProduct(productID)
            lineItem = business.LineItem(0, 1, product, 1)
            cart.addItem(lineItem)
            session['cart'] = cart
             
    products = business.getProducts()
    return render_template('products.html', products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
