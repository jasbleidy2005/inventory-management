from flask import request, jsonify, Blueprint
from ..database import db
from ..models.product import Product

product_controller = Blueprint('product_controller', __name__, url_prefix='/api')


@product_controller.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product()
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.stock = data['stock']
    product.category_id = data['category_id']
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name}), 201


@product_controller.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [{'id': p.id, 'name': p.name, 'description': p.description,
               'price': p.price, 'stock': p.stock, 'category_id': p.category_id}
              for p in products]
    return jsonify(result), 200


@product_controller.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'description': product.description,
                       'price': product.price, 'stock': product.stock, 'category_id': product.category_id}), 200
    return jsonify({'error': 'Product not found'}), 404


@product_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.stock = data['stock']
        product.category_id = data['category_id']
        db.session.commit()
        return jsonify({'id': product.id, 'name': product.name}), 200
    return jsonify({'error': 'Product not found'}), 404


@product_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return '', 204
    return jsonify({'error': 'Product not found'}), 404
