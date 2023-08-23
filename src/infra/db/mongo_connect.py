from pymongo import MongoClient
import os

class MongoConnection:
    def connect(self):
        MONGO_URL = os.getenv('MONGO_URL')
        if MONGO_URL is None:
            MONGO_URL = "mongodb://root:example@localhost:27017"

        print(f"connecting to {MONGO_URL}")
        return MongoClient(MONGO_URL)
        