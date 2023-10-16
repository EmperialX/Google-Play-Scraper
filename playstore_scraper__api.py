#!/usr/bin/env python3
from flask import Flask, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)
mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'game_data'
mongo_collection = 'games'
def get_all_apps_from_mongodb():
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]
    all_apps_data = list(collection.find({}, {'_id': 0}))
    return all_apps_data
@app.route('/api/apps', methods=['GET'])
def get_all_apps():
    all_apps_data = get_all_apps_from_mongodb()
    return jsonify(all_apps_data)
@app.route('/api/apps/<string:app_title>', methods=['GET'])
def get_app_data(app_title):
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]
    app_data = collection.find_one({'Game Title': app_title}, {'_id': 0})
    if app_data:
        return jsonify(app_data)
    else:
        return jsonify({'message': 'App not found'}), 404
if __name__ == '__main__':
    app.run(debug=True)
