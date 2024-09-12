from flask import Blueprint, request, jsonify
from ..models import db, Product

product_bp = Blueprint('product', __name__)

# Get all products
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

# Get a single product by ID
@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

# Create a new product
@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        category_id=data['category_id'],
        description=data['description'],
        price=data['price'],
        stock=data['stock'],
        image=data.get('image', None)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201
