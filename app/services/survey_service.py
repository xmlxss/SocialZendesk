import requests
from app.models import Survey
from app import db
from flask import current_app
from app.utils.event_utils import update_event_status

def send_survey(event):
    payload = {
    "template": current_app.config['INSOCIAL_TEMPLATE'],
    "fromName": "Dyflexis Support",
    "fromEmail": "info@dyflexis.com", 
    "subject": "Hoe heeft u Dyflexis Support ervaren?",
    "invites": [
        {
            "email": event.email,
            "data": {
                "agent": "Osman Kalayci",
                "location": "Den-Haag",
            }
        }
    ]
}
    headers = {
        "X-AUTH-TOKEN": current_app.config['INSOCIAL_API_KEY']
    }
    response = requests.post(f'https://api.insocial.nl/v2/customers/{current_app.config["INSOCIAL_CUSTOMERID"]}/surveys/{current_app.config["INSOCIAL_SURVEYID"]}/email-invites', headers=headers, json=payload)

    if response.status_code == 202:
        new_survey = Survey(name=f'Survey for Ticket {event.ticket_id}', status='sent', webhook_event_id=event.id)
        db.session.add(new_survey)
        db.session.commit()
        update_event_status(event, 'succeeded')
        current_app.logger.info(f'Survey sent successfully for ticket {event.ticket_id}')
    else:
        update_event_status(event, 'failed')
        current_app.logger.error(f'Failed to send survey for ticket {event.ticket_id}: Status Code {response.status_code}, Response: {response.text}')

def process_survey_sending(event):
    if event.ticket_status == 'solved':
        try:
            update_event_status(event, 'in_progress')
            send_survey(event)
        except Exception as e:
            update_event_status(event, 'failed')
            current_app.logger.error(f'Error in sending survey: {e}')

