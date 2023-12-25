from app.models import WebhookEvent, Survey
from app import db
from app.utils.event_utils import update_event_status
from app.services.survey_service import send_survey
from flask import jsonify, current_app

def process_zendesk_webhook(data):
    new_event = register_webhook_event(data)
    if new_event.ticket_status == 'solved':
        try:
            update_event_status(new_event, 'in_progress')
            send_survey(new_event)
        except Exception as e:
            update_event_status(new_event, 'failed')
            current_app.logger.error(f'Error in sending survey: {e}')
    return jsonify({'message': f'Webhook processed for id {new_event.ticket_id}'}), 200

def register_webhook_event(data):
    new_event = WebhookEvent(
        ticket_id=data.get('id'),
        ticket_priority=data.get('priority'),
        email=data.get('email'),
        ticket_status=data.get('status'),
        subject=data.get('subject'),
        description=data.get('description'),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(new_event)
    db.session.commit()
    current_app.logger.info(f'Webhook received and registered successfully for ticket {data.get("id")}')
    return new_event