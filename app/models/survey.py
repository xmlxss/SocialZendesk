from app import db

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    webhook_event_id = db.Column(db.Integer, db.ForeignKey('webhook_event.id'))

    def __repr__(self):
        return f'<Survey {self.name}>'