from pymongo import MongoClient
import os

database = os.getenv("SNAPI_DATABASE", default='snapi')
db_host  = os.getenv("SNAPI_DB_HOST", default='mongodb://127.0.0.1:27017')

def connect() -> object:
    try:
        client = MongoClient(host=db_host)
        db = client[database]
        collection = db.launchnotifications
        return collection
    except Exception as e:
        print(e)
