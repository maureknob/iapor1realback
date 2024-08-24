from flask import Flask
from flask_cors import CORS
from .routes.gpt import text_generation, image_generation, text_to_speech, speech_to_text
from .routes.payment import create_preference, process_payment


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    CORS(app)

    # gpt blueprints
    app.register_blueprint(text_generation.bp)
    app.register_blueprint(image_generation.bp)
    app.register_blueprint(text_to_speech.bp)
    app.register_blueprint(speech_to_text.bp)

    # mercado pago blueprints
    app.register_blueprint(create_preference.bp)
    app.register_blueprint(process_payment.bp)

    return app
