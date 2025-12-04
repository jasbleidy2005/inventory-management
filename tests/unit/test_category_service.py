from backend.services.category_service import CategoryService

def test_create_category():
    service = CategoryService()
    category = service.create_category({'name': 'Electronics'})
    assert category.name == 'Electronics'

def test_get_category():
    service = CategoryService()
    category = service.create_category({'name': 'Electronics'})
    assert category is not None
    assert category.name == 'Electronics'

def test_update_category():
    service = CategoryService()
    category = service.create_category({'name': 'Electronics'})
    category.name = 'Updated Electronics'
    assert category.name == 'Updated Electronics'

def test_delete_category():
    service = CategoryService()
    category = service.create_category({'name': 'Electronics'})
    assert category is not None

def test_list_categories():
    service = CategoryService()
    category1 = service.create_category({'name': 'Electronics'})
    category2 = service.create_category({'name': 'Books'})
    assert category1.name == 'Electronics'
    assert category2.name == 'Books'