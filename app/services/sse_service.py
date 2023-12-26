from app.models import WebhookEvent, Survey
from flask import Response, g, stream_with_context
import json
import time

def generate_sse_events(last_event_id, last_survey_id):
    def generate_events():
        g.last_event_id = last_event_id
        g.last_survey_id = last_survey_id

        while True:
            # Query for new webhook events
            event_query = WebhookEvent.query.filter(WebhookEvent.id > g.last_event_id).order_by(WebhookEvent.id.asc())
            new_webhook_events = event_query.limit(5).all()

            # Query for new surveys
            survey_query = Survey.query.filter(Survey.id > g.last_survey_id).order_by(Survey.id.asc())
            new_surveys = survey_query.limit(5).all()

            # Update the last IDs
            if new_webhook_events:
                g.last_event_id = new_webhook_events[-1].id
            if new_surveys:
                g.last_survey_id = new_surveys[-1].id

            # Stream new events and surveys
            for event in new_webhook_events + new_surveys:
                yield f"data: {json.dumps(event.serialize())}\n\n"

            time.sleep(5)

    return Response(stream_with_context(generate_events()), content_type='text/event-stream')