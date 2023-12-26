import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)
    ZENDESK_WEBHOOK_SECRET = os.getenv('ZENDESK_WEBHOOK_SECRET')
    INSOCIAL_API_KEY = os.getenv('INSOCIAL_API_KEY')
    INSOCIAL_TEMPLATE = os.getenv('INSOCIAL_TEMPLATE')
    INSOCIAL_CUSTOMERID = os.getenv('INSOCIAL_CUSTOMERID')
    INSOCIAL_SURVEYID = os.getenv('INSOCIAL_SURVEYID')
    FROM_EMAIL = os.getenv('FROM_EMAIL')
    FROM_COMPANY = os.getenv('FROM_COMPANY')
    SUBJECT = os.getenv('SUBJECT')
    AGENT = os.getenv('AGENT')
    LOCATION = os.getenv('LOCATION')