from app import db

def update_event_status(event, status):
    event.event_status = status
    db.session.commit()