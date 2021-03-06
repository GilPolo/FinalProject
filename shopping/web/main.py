from flask import Flask, flash, redirect, render_template, request, Response, session, abort, url_for
from random import randint
from shopping.business import business
import os

app = Flask(__name__)
app.secret_key="My Apollo Secret Key"

@app.route("/")
def index():
    if 'cart' in session:
        del session['cart']
    products = business.getProducts()
    return render_template('products.html', products=products, cart=None)

@app.route("/addtocart/",methods=['POST'])
def addCart():
    cart = None
    if request.method == 'POST':
        productID = request.form['productID']
        if 'cart' in session:
            orderID = session['cart']
            cart = business.readCart(orderID)
            product = business.getProduct(productID)
            lineItem = business.LineItem(orderID, 1, product, 1)
            cart.addItem(lineItem) 
            cart.saveCart()
        else:
            cart = business.Cart()
            product = business.getProduct(productID)
            lineItem = business.LineItem(0, 1, product, 1)
            cart.addItem(lineItem) 
            orderID=cart.createCart()
            session['cart'] = orderID
             
    products = business.getProducts()
    return render_template('products.html', products=products, cart=cart)

@app.route("/removefromcart/",methods=['POST'])
def removeFromCart():
    cart = None
    if request.method == 'POST':
        productID = int(request.form['productID'])
        if 'cart' in session:
            orderID = session['cart']
            cart = business.readCart(orderID)
            cart.removeItemByProductID(productID)
            cart.saveCart()
            if cart.getItemCount() <= 0:
                return redirect(url_for('index'))
             
    products = business.getProducts()
    return render_template('products.html', products=products, cart=cart)

@app.route("/savecart/",methods=['POST'])
def saveCart():
    cart = None
    if request.method == 'POST' and 'cart' in session:
        orderID = session['cart']
        cart = business.readCart(orderID)
        cart.status=2
        cart.saveCart()
    return render_template('saveorder.html', cart=cart)

port = int(os.getenv('PORT', 8080))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
