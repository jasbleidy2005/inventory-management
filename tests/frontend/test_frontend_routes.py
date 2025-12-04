import unittest
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from frontend.app import app as frontend_app


class TestFrontendRoutes(unittest.TestCase):
    """Pruebas para las rutas del frontend"""

    def setUp(self):
        """Configurar el cliente de prueba antes de cada test"""
        frontend_app.config['TESTING'] = True
        self.client = frontend_app.test_client()

    def tearDown(self):
        """Limpiar después de cada test"""
        pass

    def test_index_route_exists(self):
        """Probar que la ruta principal existe y retorna 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_title(self):
        """Probar que la página principal contiene el título correcto"""
        response = self.client.get('/')
        # Buscar el texto en español
        self.assertIn(b'Sistema de Inventario', response.data)

    def test_categories_route_exists(self):
        """Probar que la ruta de categorías existe"""
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

    def test_categories_page_has_content(self):
        """Probar que la página de categorías tiene el contenido esperado"""
        response = self.client.get('/categories')
        # Buscar "Categorías" en la respuesta
        self.assertIn(b'Categor', response.data)

    def test_products_route_exists(self):
        """Probar que la ruta de productos existe"""
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_products_page_has_content(self):
        """Probar que la página de productos tiene el contenido esperado"""
        response = self.client.get('/products')
        self.assertIn(b'Producto', response.data)


if __name__ == '__main__':
    unittest.main()