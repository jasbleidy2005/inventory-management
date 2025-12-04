from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_12345'

# URL del backend API
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:5000')


@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')


@app.route('/categories')
def categories():
    """Página de gestión de categorías"""
    try:
        response = requests.get(f'{BACKEND_URL}/api/categories')
        if response.status_code == 200:
            categories_list = response.json()
        else:
            categories_list = []
            flash('Error al cargar las categorías', 'error')
    except Exception as e:
        categories_list = []
        flash(f'Error de conexión: {str(e)}', 'error')
    
    return render_template('categories.html', categories=categories_list)


@app.route('/categories/create', methods=['POST'])
def create_category():
    """Crear una nueva categoría"""
    name = request.form.get('name')
    
    if not name:
        flash(' El nombre es obligatorio', 'error')
        return redirect(url_for('categories'))
    
    try:
        response = requests.post(
            f'{BACKEND_URL}/api/categories',
            json={'name': name}
        )
        
        if response.status_code == 201:
            flash(f' Categoría "{name}" creada exitosamente!', 'success')
        else:
            flash(f' Error al crear la categoría', 'error')
    except Exception as e:
        flash(f' Error de conexión: {str(e)}', 'error')
    
    return redirect(url_for('categories'))


@app.route('/categories/update/<int:category_id>', methods=['POST'])
def update_category(category_id):
    """Actualizar una categoría existente"""
    name = request.form.get('name')
    
    if not name:
        flash(' El nombre es obligatorio', 'error')
        return redirect(url_for('categories'))
    
    try:
        response = requests.put(
            f'{BACKEND_URL}/api/categories/{category_id}',
            json={'name': name}
        )
        
        if response.status_code == 200:
            flash(f' Categoría "{name}" actualizada exitosamente!', 'success')
        else:
            flash(f' Error al actualizar la categoría', 'error')
    except Exception as e:
        flash(f' Error: {str(e)}', 'error')
    
    return redirect(url_for('categories'))


@app.route('/categories/delete/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    """Eliminar una categoría"""
    try:
        response = requests.delete(f'{BACKEND_URL}/api/categories/{category_id}')
        
        if response.status_code == 200:
            flash(' Categoría eliminada exitosamente!', 'success')
        else:
            flash(' Error al eliminar la categoría', 'error')
    except Exception as e:
        flash(f' Error: {str(e)}', 'error')
    
    return redirect(url_for('categories'))


@app.route('/products')
def products():
    """Página de gestión de productos"""
    try:
        # Obtener productos
        products_response = requests.get(f'{BACKEND_URL}/api/products')
        products_list = products_response.json() if products_response.status_code == 200 else []
        
        # Obtener categorías para el formulario
        categories_response = requests.get(f'{BACKEND_URL}/api/categories')
        categories_list = categories_response.json() if categories_response.status_code == 200 else []
        
    except Exception as e:
        products_list = []
        categories_list = []
        flash(f' Error de conexión: {str(e)}', 'error')
    
    return render_template('products.html', products=products_list, categories=categories_list)


@app.route('/products/create', methods=['POST'])
def create_product():
    """Crear un nuevo producto"""
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')
    category_id = request.form.get('category_id')
    
    if not all([name, price, stock, category_id]):
        flash(' Todos los campos son obligatorios', 'error')
        return redirect(url_for('products'))
    
    try:
        response = requests.post(
            f'{BACKEND_URL}/api/products',
            json={
                'name': name,
                'description': description,
                'price': float(price),
                'stock': int(stock),
                'category_id': int(category_id)
            }
        )
        
        if response.status_code == 201:
            flash(f' Producto "{name}" creado exitosamente!', 'success')
        else:
            flash(f' Error al crear el producto', 'error')
    except Exception as e:
        flash(f' Error: {str(e)}', 'error')
    
    return redirect(url_for('products'))


@app.route('/products/update/<int:product_id>', methods=['POST'])
def update_product(product_id):
    """Actualizar un producto existente"""
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')
    category_id = request.form.get('category_id')
    
    if not all([name, price, stock, category_id]):
        flash(' Todos los campos son obligatorios', 'error')
        return redirect(url_for('products'))
    
    try:
        response = requests.put(
            f'{BACKEND_URL}/api/products/{product_id}',
            json={
                'name': name,
                'description': description,
                'price': float(price),
                'stock': int(stock),
                'category_id': int(category_id)
            }
        )
        
        if response.status_code == 200:
            flash(f' Producto "{name}" actualizado exitosamente!', 'success')
        else:
            flash(f' Error al actualizar el producto', 'error')
    except Exception as e:
        flash(f' Error: {str(e)}', 'error')
    
    return redirect(url_for('products'))


@app.route('/products/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """Eliminar un producto"""
    try:
        response = requests.delete(f'{BACKEND_URL}/api/products/{product_id}')
        
        if response.status_code == 200:
            flash(' Producto eliminado exitosamente!', 'success')
        else:
            flash(' Error al eliminar el producto', 'error')
    except Exception as e:
        flash(f' Error: {str(e)}', 'error')
    
    return redirect(url_for('products'))


if __name__ == '__main__':
    port = int(os.environ.get('FRONTEND_PORT', 5001))
    print("\n" + "="*60)
    print(f" Frontend Server Starting on http://localhost:{port}")
    print("="*60 + "\n")
    app.run(debug=True, port=port, host='0.0.0.0')