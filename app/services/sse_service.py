from app.models import WebhookEvent
from flask import Response, g, stream_with_context
import json
import time

def generate_sse_events(last_event_id):
    def generate_events():
        g.last_event_id = last_event_id
        while True:
            query = WebhookEvent.query.filter(WebhookEvent.id > g.last_event_id).order_by(WebhookEvent.id.asc())
            webhook_events = query.limit(10).all()

            if webhook_events:
                g.last_event_id = webhook_events[-1].id

            for event in webhook_events:
                event_data = {
                    "id": event.id,
                    "ticket_id": event.ticket_id,
                    "event_status": event.event_status,
                    "received_at": event.received_at.strftime('%Y-%m-%d %H:%M:%S')
                }
                yield f"data: {json.dumps(event_data)}\n\n"

            time.sleep(5)

    return Response(stream_with_context(generate_events()), content_type='text/event-stream')