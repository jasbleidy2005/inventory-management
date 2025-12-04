import os
import sys

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS

print("\n" + "="*60)
print("INITIALIZING BACKEND SERVER...")
print("="*60)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

try:
    from backend.database import db
    db.init_app(app)
    print(" Database initialized")
except Exception as e:
    print(f" Error loading database: {e}")

try:
    from backend.controllers.category_controller import category_controller
    from backend.controllers.product_controller import product_controller
    
    app.register_blueprint(category_controller)
    app.register_blueprint(product_controller)
    print(" Controllers registered")
except Exception as e:
    print(f" Error loading controllers: {e}")

@app.route('/')
def index():
    return "Welcome to the Inventory Management API"

if __name__ == '__main__':
    print("="*60)
    print(" Backend Server Starting on http://localhost:5000")
    print("="*60 + "\n")
    
    with app.app_context():
        try:
            db.create_all()
            print(" Database tables created")
        except Exception as e:
            print(f"  Database warning: {e}")
    
    app.run(host='127.0.0.1', port=5000, debug=True)