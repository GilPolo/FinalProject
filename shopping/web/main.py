from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from ..business import business

app = Flask(__name__)

@app.route("/")
def index():
    business.open()
    products = business.getProducts()
    business.close()
    return render_template('products.html', products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
