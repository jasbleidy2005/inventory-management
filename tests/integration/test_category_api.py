from flask import Flask, jsonify
import unittest
from backend.app import app, db
from backend.models.category import Category

class TestCategoryAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_category(self):
        response = self.app.post('/api/categories', json={'name': 'Test Category'})
        self.assertEqual(response.status_code, 201)

    def test_get_categories(self):
        self.app.post('/api/categories', json={'name': 'Test Category'})
        response = self.app.get('/api/categories')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Category', str(response.data))

if __name__ == '__main__':
    unittest.main()