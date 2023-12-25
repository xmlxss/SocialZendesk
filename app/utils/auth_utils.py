from flask import current_app

def validate_token(token):
    return token == current_app.config['ZENDESK_WEBHOOK_SECRET']