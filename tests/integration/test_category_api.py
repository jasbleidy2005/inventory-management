import unittest
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask
from backend.database import db
from backend.models.category import Category
from backend.controllers.category_controller import category_controller


class TestCategoryAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        db.init_app(self.app)
        self.app.register_blueprint(category_controller)
        
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_category(self):
        response = self.client.post('/api/categories', json={'name': 'Test Category'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['name'], 'Test Category')

    def test_get_categories(self):
        # Crear una categoría primero
        self.client.post('/api/categories', json={'name': 'Test Category'})
        
        # Obtener todas las categorías
        response = self.client.get('/api/categories')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(len(data) > 0)
        self.assertEqual(data[0]['name'], 'Test Category')


if __name__ == '__main__':
    unittest.main()