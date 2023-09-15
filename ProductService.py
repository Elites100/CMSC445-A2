from flask import Flask, jsonify, request
app = Flask(__name__)



# Sample product data 
products = [
  {"id": 1, "name": "Apple", "price": 0.99, "quantity": 100},
  {"id": 2, "name": "Banana", "price": 0.49, "quantity": 150},
  {"id": 3, "name": "Orange", "price": 0.79, "quantity": 80},
]



# Product Service Endpoints

# Endpoint 1: Get all available grocery products
@app.route('/products', methods = ['GET'])
def get_products():
  return jsonify({"Products": products})
  

# Endpoint 2:  Get details about a specific product by ID
@app.route('/products/<int:product_id>', methods = ['GET'])
def get_product(product_id):
   product = next((product for product in products if product["id"] == product_id), None)
   if product:
    return jsonify(product)
   else:
    return jsonify({"message": "Product not found"}), 404
  

# Endpoint 3: Create a new product
@app.route('/products', methods=['POST'])
def create_product():
  new_product = {
    "id": len(products) + 1,
    "name": request.json.get('name'),
    "price": request.json.get('price'),
    "quantity": request.json.get('quantity')
  }
  products.append(new_product)
  return jsonify({"message": "Product created", "Product": new_product}), 201
 

if __name__ == '__main__':
    app.run()
