from flask import Blueprint, request, jsonify
from ..models import db, Cart, CartItem

cart_bp = Blueprint('cart', __name__)

# Get current cart for a user
@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({"message": "Cart not found"}), 404
    return jsonify(cart.to_dict())

# Add an item to the cart
@cart_bp.route('/cart/<int:user_id>/items', methods=['POST'])
def add_to_cart(user_id):
    data = request.get_json()
    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()

    new_cart_item = CartItem(
        cart_id=cart.id,
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify(new_cart_item.to_dict()), 201
