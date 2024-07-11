from flask import Blueprint, request, jsonify
from app.services.payment_service import create_preference

bp = Blueprint('create_preference', __name__)

@bp.route('/payment/create-preference', methods=['POST'])
def generate():
    data = request.get_json()
    response = create_preference(data)
    return jsonify(response)