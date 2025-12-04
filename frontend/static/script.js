document.addEventListener('DOMContentLoaded', function() {
    const categoryForm = document.getElementById('category-form');
    const productForm = document.getElementById('product-form');
    const productList = document.getElementById('product-list');
    const categoryList = document.getElementById('category-list');

    // Function to fetch categories and populate the category list
    function fetchCategories() {
        fetch('/api/categories')
            .then(response => response.json())
            .then(data => {
                categoryList.innerHTML = '';
                data.forEach(category => {
                    const li = document.createElement('li');
                    li.textContent = category.name;
                    categoryList.appendChild(li);
                });
            });
    }

    // Function to fetch products and populate the product list
    function fetchProducts() {
        fetch('/api/products')
            .then(response => response.json())
            .then(data => {
                productList.innerHTML = '';
                data.forEach(product => {
                    const li = document.createElement('li');
                    li.textContent = `${product.name} - ${product.price} - ${product.stock}`;
                    productList.appendChild(li);
                });
            });
    }

    // Event listener for category form submission
    categoryForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(categoryForm);
        fetch('/api/categories', {
            method: 'POST',
            body: formData
        }).then(() => {
            fetchCategories();
            categoryForm.reset();
        });
    });

    // Event listener for product form submission
    productForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(productForm);
        fetch('/api/products', {
            method: 'POST',
            body: formData
        }).then(() => {
            fetchProducts();
            productForm.reset();
        });
    });

    // Initial fetch of categories and products
    fetchCategories();
    fetchProducts();
});