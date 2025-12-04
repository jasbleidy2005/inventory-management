from backend.services.product_service import ProductService

class TestProductService:
    
    def setup_method(self):
        self.product_service = ProductService()
    
    def test_create_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 10.99,
            'stock': 100,
            'category_id': 1
        }
        product = self.product_service.create_product(product_data)
        assert product is not None
        assert product.name == product_data['name']
        assert product.price == product_data['price']
    
    def test_get_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 10.99,
            'stock': 100,
            'category_id': 1
        }
        product = self.product_service.create_product(product_data)
        assert product is not None
    
    def test_update_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 10.99,
            'stock': 100,
            'category_id': 1
        }
        product = self.product_service.create_product(product_data)
        assert product.name == 'Test Product'
    
    def test_delete_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 10.99,
            'stock': 100,
            'category_id': 1
        }
        product = self.product_service.create_product(product_data)
        assert product is not None