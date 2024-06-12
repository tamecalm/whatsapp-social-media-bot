from flask import Blueprint, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from app.utils import handle_message

bp = Blueprint('routes', __name__)

@bp.route('/webhook', methods=['POST'])
def webhook():
    message = request.form.get('Body')
    sender = request.form.get('From')

    response_message = handle_message(message, sender)
    
    response = MessagingResponse()
    response.message(response_message)

    return str(response)
