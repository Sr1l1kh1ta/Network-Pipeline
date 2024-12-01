import boto3
import json
import random
import time
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

# AWS Kinesis client
kinesis = boto3.client('kinesis', region_name='us-east-1')  # Replace with your region

# Kinesis stream name
stream_name = 'clickstream'  # Replace with your stream name

# List of possible page URLs and element IDs
page_urls = [
    'https://www.example.com/home',
    'https://www.example.com/product/123',
    'https://www.example.com/cart',
    'https://www.example.com/checkout'
]

element_ids = [
    'add_to_cart_button',
    'place_order_button',
    'product_image',
    'search_button',
    'login_button'
]

# Function to generate a random clickstream event
def generate_event(user_id, session_id, timestamp):
    event_id = fake.uuid4()
    page_url = random.choice(page_urls)
    event_type = random.choice(['page_view', 'click', 'purchase'])
    element_id = random.choice(element_ids) if event_type == 'click' else None
    location = {
        'city': fake.city(),
        'country': fake.country()
    }
    device = {
        'type': random.choice(['desktop', 'mobile']),
        'os': random.choice(['Windows', 'MacOS', 'Linux', 'Android', 'iOS'])
    }

    event = {
        'event_id': event_id,
        'timestamp': timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'user_id': user_id,
        'session_id': session_id,
        'page_url': page_url,
        'event_type': event_type,
        'element_id': element_id,
        'location': location,
        'device': device
    }

    return event

# Function to send events to Kinesis
def send_to_kinesis(events):
    records = [
        {
            'Data': json.dumps(event),
            'PartitionKey': event['user_id']
        }
        for event in events
    ]

    response = kinesis.put_records(
        Records=records,
        StreamName=stream_name
    )

    return response

# Generate and send events for a single session
def generate_session_events(user_id, session_id, start_time, num_events):
    events = [generate_event(user_id, session_id, start_time + timedelta(seconds=i)) for i in range(num_events)]
    send_to_kinesis(events)

# Generate multiple sessions
def main():
    num_sessions = random.randint(1, 10)  # Random number of sessions
    for _ in range(num_sessions):
        user_id = fake.uuid4()
        session_id = fake.uuid4()
        start_time = datetime.utcnow()
        num_events = random.randint(1, 6)  # Random number of events per session

        generate_session_events(user_id, session_id, start_time, num_events)

        # Random delay between 1 and 20 seconds
        delay = random.randint(1, 10)
        time.sleep(delay)

if __name__ == '__main__':
    main()