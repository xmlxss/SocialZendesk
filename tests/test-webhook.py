import requests
import random
from time import sleep

url = 'http://localhost:5000/webhook/zendesk'
def generate_random_id():
    return random.randint(1, 1000)

def random_status():
    return random.choice(['solved'])

def webhook_event(id):
    data = {
        'ticket': {
            'id': id,
            'priority': 'urgent',
            'email': 'test@mail.com',
            'status': random_status(),
            'subject': 'Test ticket',
            'description': 'This is a test ticket',
            'tags': ['test', 'urgent']
        }
    }
    headers = {
        "Authorization": "1234"
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())

if __name__ == '__main__':
    while True:
        sleep(3)
        webhook_event(generate_random_id())
