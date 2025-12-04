import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from frontend.app import app


class TestFrontendRoutes(unittest.TestCase):
    def setUp(self):
        """Configurar el cliente de prueba"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_route_exists(self):
        """Verificar que la ruta principal existe y responde"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_title(self):
        """Verificar que la página principal contiene el título"""
        response = self.client.get('/')
        # Cambiar a contenido en inglés que está en el template
        self.assertIn(b'Inventory Management', response.data)

    def test_categories_route_exists(self):
        """Verificar que la ruta de categorías existe"""
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

    def test_categories_page_has_content(self):
        """Verificar que la página de categorías tiene contenido esperado"""
        response = self.client.get('/categories')
        # Buscar contenido que exista en el template
        self.assertIn(b'Categor', response.data)

    def test_products_route_exists(self):
        """Verificar que la ruta de productos existe"""
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_products_page_has_content(self):
        """Verificar que la página de productos tiene contenido esperado"""
        response = self.client.get('/products')
        # Cambiar a "Product" en inglés
        self.assertIn(b'Product', response.data)


if __name__ == '__main__':
    unittest.main()