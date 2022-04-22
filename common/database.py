import pymongo
from typing import Dict
class Database:
    URI = "mongodb://127.0.0.1/2701/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()  #this is the database that is created in mongodb

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data) 