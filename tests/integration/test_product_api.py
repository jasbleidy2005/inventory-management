import unittest
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask
from backend.database import db
from backend.models.product import Product
from backend.models.category import Category
from backend.controllers.product_controller import product_controller
from backend.controllers.category_controller import category_controller

class ProductApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        db.init_app(self.app)
        self.app.register_blueprint(category_controller)
        self.app.register_blueprint(product_controller)
        
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
            # Crear una categoría de prueba
            category = Category()
            category.name = 'Test Category'
            db.session.add(category)
            db.session.commit()
            self.category_id = category.id
            
        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 10.99,
            'stock': 100,
            'category_id': self.category_id
        }

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product(self):
        response = self.client.post('/api/products', json=self.product_data)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)

    def test_get_product(self):
        response = self.client.post('/api/products', json=self.product_data)
        product_id = response.get_json()['id']
        
        response = self.client.get(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], self.product_data['name'])

    def test_update_product(self):
        response = self.client.post('/api/products', json=self.product_data)
        product_id = response.get_json()['id']
        
        updated_data = {
            'name': 'Updated Product',
            'description': 'This is an updated test product',
            'price': 12.99,
            'stock': 80,
            'category_id': self.category_id
        }
        response = self.client.put(f'/api/products/{product_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], updated_data['name'])

    def test_delete_product(self):
        response = self.client.post('/api/products', json=self.product_data)
        product_id = response.get_json()['id']
        
        response = self.client.delete(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 204)
        
        response = self.client.get(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()