from ..models.product import Product


class ProductService:
    def create_product(self, data):
        product = Product()
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.stock = data['stock']
        product.category_id = data['category_id']
        return product

    def get_all_products(self):
        return []

    def get_product_by_id(self, product_id):
        return None

    def update_product(self, product_id, data):
        return None

    def delete_product(self, product_id):
        pass
