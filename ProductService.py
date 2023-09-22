from flask import Flask, jsonify, request
app = Flask(__name__)
import os



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

# Endpoint 4: Deleting a product
@app.route('/products/remove/<int:product_id>', methods=['POST'])
def remove_product(product_id):

  # Find the product in the Sample product data list
  product_index = None
  for i, product in enumerate(products):
    if product['id'] == product_id:
      product_index = i
      break

  if product_index is None:
    return jsonify({"error": "Product not found"}), 404
  
  # specify the amount to remove or default to 1
  remove_quantity = request.json.get('quantity', 1)

  if remove_quantity <= 0:
    return jsonify({"error": "Invalid quantity"}), 400

  if products[product_index]['quantity'] < remove_quantity:
    return jsonify({"error": "Insufficient quantity"}), 400
  
  # Subtract the quantity from the Sample product data by ID
  products[product_index]['quantity'] -= remove_quantity

  # If quantity becomes 0, you can remove the product from the list
  if products[product_index]['quantity'] == 0:
    del products[product_index]
  
  return jsonify({"message": "Quantity removed", "Product": products[product_index]}), 200
 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port) # might need to change in RENDER
