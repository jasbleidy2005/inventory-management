from flask import Flask, jsonify
import unittest
from backend.app import app, db
from backend.models.product import Product
from backend.models.category import Category

class ProductApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()
            self.category = Category()
            self.category.name = 'Test Category'
            db.session.add(self.category)
            db.session.commit()
            self.product_data = {
                'name': 'Test Product',
                'description': 'This is a test product',
                'price': 10.99,
                'stock': 100,
                'category_id': self.category.id
            }

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product(self):
        response = self.app.post('/api/products', json=self.product_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_product(self):
        response = self.app.post('/api/products', json=self.product_data)
        product_id = response.get_json()['id']
        response = self.app.get(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], self.product_data['name'])

    def test_update_product(self):
        response = self.app.post('/api/products', json=self.product_data)
        product_id = response.get_json()['id']
        updated_data = {
            'name': 'Updated Product',
            'description': 'This is an updated test product',
            'price': 12.99,
            'stock': 80,
            'category_id': self.category.id
        }
        response = self.app.put(f'/api/products/{product_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], updated_data['name'])

    def test_delete_product(self):
        response = self.app.post('/api/products', json=self.product_data)
        product_id = response.get_json()['id']
        response = self.app.delete(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/api/products/{product_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()