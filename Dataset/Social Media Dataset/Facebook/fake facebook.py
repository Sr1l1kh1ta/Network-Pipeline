import json
import random
from datetime import datetime, timedelta

# Function to generate a random user ID
def generate_user_id():
    return ''.join(random.choices('0123456789', k=9))

# Function to generate a random username
def generate_username():
    prefixes = ['John', 'Jane', 'Alice', 'Bob', 'Emily', 'Michael', 'Emma', 'David']
    suffixes = ['Doe', 'Smith', 'Johnson', 'Brown', 'Wilson']
    return random.choice(prefixes) + ' ' + random.choice(suffixes)

# Function to generate a random profile picture URL
def generate_profile_picture():
    return f"https://example.com/{generate_username().lower().replace(' ', '_')}_profile_picture.jpg"

# Function to generate a random comment
def generate_comment():
    comments = ['Great post!', 'Congratulations!', 'Looks interesting.', 'Well done!', 'Amazing!', 'Exciting news!']
    return random.choice(comments)

# Function to generate a random Facebook post
def generate_post(post_id):
    return {
        "post_id": str(post_id),
        "author": {
            "user_id": generate_user_id(),
            "username": "ABC Corp",
            "profile_picture": generate_profile_picture()
        },
        "text": "Excited to announce the launch of our latest product!",
        "created_at": (datetime.utcnow() - timedelta(days=random.randint(0, 30))).isoformat() + "Z",
        "likes": [
            {
                "user_id": generate_user_id(),
                "username": generate_username(),
                "profile_picture": generate_profile_picture()
            }
            for _ in range(random.randint(0, 10))
        ],
        "comments": [
            {
                "comment_id": generate_user_id(),
                "user": {
                    "user_id": generate_user_id(),
                    "username": generate_username(),
                    "profile_picture": generate_profile_picture()
                },
                "text": generate_comment(),
                "created_at": (datetime.utcnow() - timedelta(days=random.randint(0, 30))).isoformat() + "Z",
                "likes": [
                    {
                        "user_id": generate_user_id(),
                        "username": generate_username(),
                        "profile_picture": generate_profile_picture()
                    }
                    for _ in range(random.randint(0, 5))
                ]
            }
            for _ in range(random.randint(0, 5))
        ]
    }

# Function to generate a sample dataset
def generate_dataset(num_posts):
    posts = [generate_post(post_id) for post_id in range(1, num_posts + 1)]
    return {"posts": posts}

# Generate and save the dataset to a JSON file
sample_data = generate_dataset(100)
with open("C:/Users/srilikhita.balla/Downloads/abc_corp_facebook_data.json", "w") as json_file:
    json.dump(sample_data, json_file, indent=4)

print("Sample dataset generated and saved successfully!")
