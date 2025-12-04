from flask import request, jsonify, Blueprint
from ..database import db
from ..models.category import Category

category_controller = Blueprint('category_controller', __name__, url_prefix='/api')


@category_controller.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category = Category()
    category.name = data['name']
    db.session.add(category)
    db.session.commit()
    return jsonify({'id': category.id, 'name': category.name}), 201


@category_controller.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    result = [{'id': c.id, 'name': c.name} for c in categories]
    return jsonify(result), 200


@category_controller.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = db.session.get(Category, category_id)
    if category:
        return jsonify({'id': category.id, 'name': category.name}), 200
    return jsonify({'error': 'Category not found'}), 404


@category_controller.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = db.session.get(Category, category_id)
    if category:
        data = request.get_json()
        category.name = data['name']
        db.session.commit()
        return jsonify({'id': category.id, 'name': category.name}), 200
    return jsonify({'error': 'Category not found'}), 404


@category_controller.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = db.session.get(Category, category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return '', 204
    return jsonify({'error': 'Category not found'}), 404