from app import db
from datetime import datetime

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    webhook_event_id = db.Column(db.Integer, db.ForeignKey('webhook_event.id'))
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)  

    def serialize(self):
        return {
            "id": self.id,
            "type": "survey",
            "name": self.name,
            "status": self.status,
            "webhook_event_id": self.webhook_event_id,
            "sent_at": self.sent_at.strftime('%Y-%m-%d %H:%M:%S') if self.sent_at else 'N/A'  
        }

    def __repr__(self):
        return f'<Survey {self.name}>'