import requests
import random
from time import sleep

url = 'http://127.0.0.1:5000/webhook/zendesk'
def generate_random_id():
    return random.randint(1, 1000)

def random_status():
    return random.choice(['solved'])

def webhook_event(id):
    data = {
        'ticket': {
            'id': id,
            'priority': 'urgent',
            'email': 'osman.kalayci@dyflexis.com',
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
    print(response.status_code)
    if response.ok:
        print(response.json())
    else:
        print("Error: ", response.text)

if __name__ == '__main__':
    while True:
        sleep(3)
        webhook_event(generate_random_id())
