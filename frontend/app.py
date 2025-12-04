from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

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
        categories = response.json() if response.status_code == 200 else []
    except Exception as e:
        categories = []
        print(f"Error: {e}")
    return render_template('categories.html', categories=categories)


@app.route('/products')
def products():
    """Página de gestión de productos"""
    try:
        response = requests.get(f'{BACKEND_URL}/api/products')
        products = response.json() if response.status_code == 200 else []
        
        response_cat = requests.get(f'{BACKEND_URL}/api/categories')
        categories = response_cat.json() if response_cat.status_code == 200 else []
    except Exception as e:
        products = []
        categories = []
        print(f"Error: {e}")
    return render_template('products.html', products=products, categories=categories)


if __name__ == '__main__':
    print("\n" + "="*60)
    print(" Frontend Server Starting on http://localhost:5001")
    print("="*60 + "\n")
    app.run(host='127.0.0.1', port=5001, debug=True)  # Cambiar a puerto 5001