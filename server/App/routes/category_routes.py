from flask import Blueprint, request, jsonify
from ..models import db, Category

category_bp = Blueprint('category', __name__)

# Get all categories
@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

# Create a new category
@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(
        name=data['name'],
        description=data.get('description', '')
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.to_dict()), 201
