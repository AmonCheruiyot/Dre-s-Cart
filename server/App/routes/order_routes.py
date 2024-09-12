from flask import Blueprint, request, jsonify
from ..models import db, Order

order_bp = Blueprint('order', __name__)

# Create a new order
@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        user_id=data['user_id'],
        total_price=data['total_price'],
        is_paid=data['is_paid'],
        payment_date=data.get('payment_date', None)
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# Get a single order by ID
@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_dict())
