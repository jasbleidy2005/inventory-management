import sys
import os

# Agregar el directorio padre al path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

from backend.database import db
db.init_app(app)

from backend.controllers.category_controller import category_controller
from backend.controllers.product_controller import product_controller

app.register_blueprint(category_controller)
app.register_blueprint(product_controller)


@app.route('/')
def index():
    return "Welcome to the Inventory Management API"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='127.0.0.1', port=5000)  # nosec B104