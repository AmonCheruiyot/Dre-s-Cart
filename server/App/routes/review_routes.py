from flask import Blueprint, request, jsonify
from ..models import db, Review

review_bp = Blueprint('review', __name__)

# Get reviews for a product
@review_bp.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    return jsonify([review.to_dict() for review in reviews])

# Create a new review
@review_bp.route('/products/<int:product_id>/reviews', methods=['POST'])
def create_review(product_id):
    data = request.get_json()
    new_review = Review(
        product_id=product_id,
        user_id=data['user_id'],
        rating=data['rating'],
        comment=data.get('comment', '')
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201
