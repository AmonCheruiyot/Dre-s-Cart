from flask import Blueprint, request, jsonify
from ..models import db, Payment

payment_bp = Blueprint('payment', __name__)

# Process a payment
@payment_bp.route('/payments', methods=['POST'])
def process_payment():
    data = request.get_json()
    new_payment = Payment(
        order_id=data['order_id'],
        amount=data['amount'],
        payment_method=data['payment_method'],
        payment_date=data.get('payment_date', None)
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201
