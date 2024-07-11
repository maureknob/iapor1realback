from flask import Blueprint, request, jsonify
from app.services.gpt_service import text_to_speech

bp = Blueprint('text_to_speech', __name__, url_prefix='/text-to-speech')

@bp.route('/', methods=['POST', 'OPTIONS'])
def convert():
    data = request.get_json()
    text = data.get('text')
    response = text_to_speech(text)
    return jsonify(response)
