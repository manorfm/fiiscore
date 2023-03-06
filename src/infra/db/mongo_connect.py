from pymongo import MongoClient

class MongoConnection:
    def connect(self):
        return MongoClient("mongodb://root:example@localhost:27017")
        