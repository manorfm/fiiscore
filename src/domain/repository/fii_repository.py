from src.infra.db.mongo_connect import MongoConnection
from src.domain.model.fii import FII

class FIIRepository:
    
    def get(self, fii: FII) -> FII | None:
        mongo = MongoConnection()
        client = mongo.connect()
        with client:
            db = client.fii_manager
            return db.fii.find_one({ "name": fii.name })

    def persist(self, fii: FII):
        mongo = MongoConnection()
        client = mongo.connect()
        with client:
            db = client.fii_manager
            db.fii.insert_one({ "name": fii.name })
            
            
    def get_all(self):
        mongo = MongoConnection()
        client = mongo.connect()
        with client:
            db = client.fii_manager
            cursor = db.fii.find({})
            return list(cursor)
