from flask import Flask, jsonify, request

app = Flask(_name_)

# In-memory product list for simplicity
products = []

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)