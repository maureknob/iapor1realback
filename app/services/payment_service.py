import mercadopago
from flask import current_app as app



def create_preference(data):
    with app.app_context():
        sdk = mercadopago.SDK(app.config['ACCESS_TOKEN'])
        preference_data = {
            "items": [
                {
                    "title": data.get("title", "Product Title"),
                    "quantity": data.get("quantity", 1),
                    "unit_price": data.get("unit_price", 100.0)
                }
            ],
            "payer": {
                "email": data.get("email", "payer_email@example.com")
            },
            "back_urls": {
                "success": "google.com",
                "failure": data.get("failure_url", "http://localhost:5000/failure"),
                "pending": data.get("pending_url", "http://localhost:5000/pending")
            },
            "auto_return": "approved"
        }
        
        preference_response = sdk.preference().create(preference_data)
        return preference_response["response"]

def process_payment(data):
    try:
        print('Payload recebido:', data)
        
        sdk = mercadopago.SDK(app.config['ACCESS_TOKEN'])
        payment_response = sdk.payment().create(data)
        return payment_response["response"]
    
    except Exception as e:
        error_message = str(e)
        return {"error": error_message}