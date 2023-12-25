import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)
    ZENDESK_WEBHOOK_SECRET = 'SECRET KEY'
    INSOCIAL_API_KEY = 'SECRET KEY'
    INSOCIAL_TEMPLATE = 'tenant id'
    INSOCIAL_CUSTOMERID = 'tenant id'
    INSOCIAL_SURVEYID = 'survey id'
    FROM_EMAIL = 'email'
    FROM_COMPANY = 'company name'
    SUBJECT = 'subject'
    AGENT = 'agent'
    LOCATION = 'location'