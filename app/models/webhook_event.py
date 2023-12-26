from app import db
from datetime import datetime

class WebhookEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, nullable=False)
    ticket_priority = db.Column(db.String(64))
    email = db.Column(db.String(120))
    ticket_status = db.Column(db.String(64))
    subject = db.Column(db.String(255))
    description = db.Column(db.Text)
    tags = db.Column(db.Text)  
    received_at = db.Column(db.DateTime, default=datetime.utcnow)
    event_status = db.Column(db.String(64), default='pending')  
    def serialize(self):
        return {
            "id": self.id,
            "type": "webhook_event",
            "ticket_id": self.ticket_id,
            "ticket_priority": self.ticket_priority,
            "email": self.email,
            "ticket_status": self.ticket_status,
            "subject": self.subject,
            "description": self.description,
            "tags": self.tags,
            "received_at": self.received_at.strftime('%Y-%m-%d %H:%M:%S'),
            "event_status": self.event_status
        }

    def __repr__(self):
        return f'<WebhookEvent Ticket {self.ticket_id}>'