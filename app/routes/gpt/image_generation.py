from flask import Blueprint, request, jsonify
from app.services.gpt_service import generate_image

bp = Blueprint('image_generation', __name__)

@bp.route('/image-generation', methods=['POST'])
def generate():    
    data = request.get_json()
    prompt = data.get('prompt')
    response = generate_image(prompt)
    return jsonify(response)