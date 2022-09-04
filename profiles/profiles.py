from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

DBClient = MongoClient(DATABASE_URL)

# method that takes a dictionary and inserts it into the mongodb profiles dict


def insertProfile(ProfDict):
    db = DBClient.test
    collection = db.profiles  # the profiles object
    data = collection.find()  # all the data inside profiles
    collection.insert_one(ProfDict)
