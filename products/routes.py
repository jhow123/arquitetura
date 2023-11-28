# products/routes.py
from flask import Flask, request, jsonify
from products.models import Product

app = Flask(__name__)

products = []

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(id=len(products) + 1, name=data['name'], price=data['price'])
    products.append(product)
    return jsonify({"id": product.id, "name": product.name, "price": product.price}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products_data = [{"id": product.id, "name": product.name, "price": product.price} for product in products]
    return jsonify(products_data)
