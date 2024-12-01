import random
from datetime import datetime, timedelta

# Sample tweet texts
tweet_texts = [
    "Excited to announce our latest product launch! Introducing the ABC SmartWatch - your ultimate companion for a connected lifestyle. #ABCSmartWatch",
    "Big news! Our ABC Home Assistant now comes with advanced AI capabilities, making your home smarter than ever. #ABCHomeAssistant",
    "Introducing the ABC SmartSpeaker - your voice-controlled assistant for the modern home. #ABCSmartSpeaker",
    "Experience immersive entertainment with the ABC VR Headset. Dive into virtual worlds like never before. #ABCVR",
    "Join us for an exclusive webinar on the future of technology. Don't miss out on valuable insights! #ABCTechWebinar"
]

# Sample usernames and profile descriptions
usernames = ["tech_enthusiast", "gadgetlover", "wearable_fanatic", "smarthome_enthusiast", "homeautomation_guru", "home_tech_lover", "AI_enthusiast", "tech_influencer"]
profile_descriptions = [
    "Passionate about technology and innovation.",
    "Always on the lookout for the latest gadgets.",
    "Obsessed with wearable technology.",
    "Transforming homes into smart spaces.",
    "Expert in home automation solutions.",
    "Passionate about tech innovations for the home.",
    "Fascinated by artificial intelligence.",
    "Sharing insights about tech trends."
]

# Function to generate random retweets and likes for a tweet
def generate_interactions():
    retweet_count = random.randint(0, 10)
    like_count = random.randint(0, 20)
    retweets = []
    likes = []

    for _ in range(retweet_count):
        retweet = {
            "user_id": random.randint(1000, 9999),
            "username": random.choice(usernames),
            "profile_description": random.choice(profile_descriptions),
            "retweet_time": generate_timestamp()
        }
        retweets.append(retweet)

    for _ in range(like_count):
        like = {
            "user_id": random.randint(1000, 9999),
            "username": random.choice(usernames),
            "profile_description": random.choice(profile_descriptions),
            "like_time": generate_timestamp()
        }
        likes.append(like)

    return retweets, likes

# Function to generate a random timestamp
def generate_timestamp():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.isoformat()

# Function to generate a tweet with interactions
def generate_tweet(tweet_id, text):
    retweets, likes = generate_interactions()
    tweet = {
        "tweet_id": tweet_id,
        "text": text,
        "created_at": generate_timestamp(),
        "retweets": retweets,
        "likes": likes
    }
    return tweet

# Function to generate a dataset with tweets
def generate_dataset(num_tweets):
    tweets = []
    for i in range(1, num_tweets + 1):
        tweet_text = random.choice(tweet_texts)
        tweet = generate_tweet(i, tweet_text)
        tweets.append(tweet)
    return tweets

# Generate 100 tweets dataset
dataset = generate_dataset(100)

# Print the dataset
import json
with open("C:/Users/srilikhita.balla/Downloads/fake_tweets.json", "w") as file:
    
    json.dump({"tweets": dataset}, file, indent=2)

print("Dataset saved to fake_tweets.json")