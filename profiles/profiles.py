from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

DBClient = MongoClient(DATABASE_URL)

# profdict: {
# userID: 1234
# chID: 5678
# points: 1
# }

db = DBClient.test
collection = db.profiles  # the profiles object
data = collection.find()  # all the data inside profiles

# method that takes a dictionary and inserts it into the mongodb profiles dict


def InsertProfile(ProfDict):
    collection.insert_one(ProfDict)


# returns the profile from the database, 'bruh what' on error
def PullProfile(ProfDict):
    x = collection.find_one(ProfDict)
    if x == None:  # there are no matches
        return 'bruh what'
    else:  # the profile exists
        return x
