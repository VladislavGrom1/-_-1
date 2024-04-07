
from pymongo import MongoClient

def connection():
    client = MongoClient('localhost', 27017)
    db = client['OnlineCinema']
    cinema = db['Cinema']
    actors = db['Actors']
    films = db['Films']
    return client, db, cinema, actors, films
