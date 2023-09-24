import random
import os
from google_play_scraper import app, search
import time
from pymongo import MongoClient
mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'game_data111'
mongo_collection = 'games'
categories = [
    'Action-games' + random.choice(['', 's']),
    'Adventure-games' + random.choice(['', 's']),
    'Arcade-games' + random.choice(['', 's']),
    'Board-games' + random.choice(['', 's']),
    'Card-games' + random.choice(['', 's']),
    'Casino-games' + random.choice(['', 's']),
    'Casual-games' + random.choice(['', 's']),
    'Educational-games' + random.choice(['', 's']),
    'Music-games' + random.choice(['', 's']),
    'Puzzle-games' + random.choice(['', 's']),
    'Role-Playing-games' + random.choice(['', 's']),
    'Simulation-games' + random.choice(['', 's']),
    'Sports-games' + random.choice(['', 's']),
    'Strategy-games' + random.choice(['', 's']),
    'Trivia-games' + random.choice(['', 's']),
    'Word-games' + random.choice(['', 's']),
    'Racing-games' + random.choice(['', 's']),
    'Classic-games' + random.choice(['', 's']),
    'Board-games' + random.choice(['', 's']),
    'Card-games' + random.choice(['', 's']),
    'Casino-games' + random.choice(['', 's']),
    'Educational-games' + random.choice(['', 's']),
    'Music-games' + random.choice(['', 's']),
    'Puzzle-games' + random.choice(['', 's']),
    'Role-Playing-games' + random.choice(['', 's']),
    'Simulation-games' + random.choice(['', 's']),
    'Sports-games' + random.choice(['', 's']),
    'Strategy-games' + random.choice(['', 's']),
    'Trivia-games' + random.choice(['', 's']),
    'Word-games' + random.choice(['', 's']),
    'Racing-games' + random.choice(['', 's']),
    'Classic-games' + random.choice(['', 's']),
    'Casino-games' + random.choice(['', 's']),
    'Educational-games' + random.choice(['', 's']),
    'Music-games' + random.choice(['', 's']),
    'Puzzle-games' + random.choice(['', 's']),
    'Role-Playing-games' + random.choice(['', 's']),
    'Simulation-games' + random.choice(['', 's']),
    'Sports-games' + random.choice(['', 's']),
    'Strategy-games' + random.choice(['', 's']),
    'Trivia-games' + random.choice(['', 's']),
    'Word-games' + random.choice(['', 's']),
    'Racing-games' + random.choice(['', 's']),
    'Classic-games' + random.choice(['', 's']),
]
max_apps = 10000
def clean_file_name(name):
    return "".join([c for c in name if c.isalnum() or c in (' ', '_', '-')])
def scrape_and_save_data():
    app_count = 0
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]
    while app_count < max_apps:
        game_titles = set()
        for _ in range(len(categories)):
            random_category = random.choice(categories)
            results = search(random_category)
            for result in results:
                app_id = result['appId']
                app_info = app(app_id)
                required_fields = {
                    'Game Title': app_info['title'],
                    'Category Tags': app_info.get('genre', 'N/A'),
                    'Game Version': app_info.get('version', 'N/A'),
                    'Last Updated On': app_info.get('updated', 'N/A'),
                    'Released On': app_info.get('released', 'N/A'),
                    'In-App Purchase Required': not app_info.get('free', True),
                    'Developer Website': app_info.get('developerWebsite', 'N/A'),
                    'Phone Number': 'N/A',  # You may not have a direct phone number in this structure
                    'Support Email': app_info.get('developerEmail', 'N/A'),
                    'Address': app_info.get('developerAddress', 'N/A'),
                }
                game_title = clean_file_name(required_fields['Game Title'])
                if not collection.find_one({'Game Title': game_title}):
                    collection.insert_one(required_fields)
                    app_count += 1
                    if app_count >= max_apps:
                        break
            if app_count >= max_apps:
                break
        time.sleep(3600)
if __name__ == '__main__':
    scrape_and_save_data()
