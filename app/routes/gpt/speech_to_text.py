from flask import Blueprint, request, jsonify
from app.services.gpt_service import speech_to_text

bp = Blueprint('speech_to_text', __name__, url_prefix='/speech-to-text')

@bp.route('/', methods=['POST', 'OPTIONS'])
def convert():
    data = request.get_json()
    audio = data.get('audio')
    response = speech_to_text(audio)
    return jsonify(response)
