from flask import Flask, flash, redirect, render_template, request, Response, session, abort
from random import randint
from shopping.business import business

app = Flask(__name__)

@app.route("/")
def index():
    products = business.getProducts()
    return render_template('products.html', products=products)

@app.route("/addtocart/",methods=['POST'])
def addCart():
    if request.method == 'POST':
        print(request.form)
        productID = request.form['addtocart']
        print("Product selected= ", str(productID))
    products = business.getProducts()
    return render_template('products.html', products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
