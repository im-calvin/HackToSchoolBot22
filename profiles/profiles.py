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


# method that takes a dictionary and inserts it into the mongodb profiles dict

def PullAll():
    # all the data inside profiles
    data = collection.find().sort('points', direction=-1)
    return data


def InsertProfile(ProfDict):
    collection.insert_one(ProfDict)


def UpdateProfile(points, mongoID, ProfDict):
    x = collection.find_one(ProfDict)
    newvalues = {
        "$set": {
            'points': points}
    }
    filter = {
        '_id': mongoID
    }
    collection.update_one(
        filter, newvalues)

# returns the profile from the database, 'bruh what' on error


def PullProfile(userID, chID):
    ProfDict = {
        'userID': userID,
        'chID': chID
    }
    x = collection.find_one(ProfDict)
    if x == None:  # there are no matches
        return 'bruh what'
    else:  # the profile exists
        return x
