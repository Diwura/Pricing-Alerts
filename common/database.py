from gc import collect
import pymongo
from typing import Dict
class Database:
    URI = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()  #this is the database that is created in mongodb

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert_one(data) 
#this method finds all the items or specific items in our database.
    @staticmethod
    def find(collection:str, query:Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query) 

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query:Dict, data: Dict) -> None:
        Database.DATABASE[collection].replace_one(query, data, upsert=True)

    @staticmethod
    def remove(collection:str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove_one(query)

    