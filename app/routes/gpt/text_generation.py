from flask import Blueprint, request, jsonify
from app.services.gpt_service import generate_text

bp = Blueprint('text_generation', __name__, url_prefix='/text-generation')

@bp.route('/', methods=['POST', 'OPTIONS'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    response = generate_text(prompt)
    return jsonify(response)
