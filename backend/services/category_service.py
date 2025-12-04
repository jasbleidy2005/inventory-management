from ..models.category import Category


class CategoryService:
    def create_category(self, data):
        category = Category()
        category.name = data['name']
        return category

    def get_all_categories(self):
        return []

    def get_category_by_id(self, category_id):
        return None

    def update_category(self, category_id, data):
        return None

    def delete_category(self, category_id):
        pass
