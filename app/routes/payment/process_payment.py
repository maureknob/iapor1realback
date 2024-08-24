from flask import Blueprint, request, jsonify
from app.services.payment_service import process_payment

bp = Blueprint('process_payment', __name__)

@bp.route('/payment/process-payment', methods=['POST'])
def generate():
    data = request.get_json()
    response = process_payment(data)
    return jsonify(response)