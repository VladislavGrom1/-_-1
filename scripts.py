from bson import ObjectId
from pymongo import MongoClient
from connectMongo import connection

# Соединение с MongoDB
client, db, cinema, actors, films = connection()

# Поиск актёра по имени
def searchActor(nameActor):
    itemActor = actors.find_one({'Name': nameActor})
    return itemActor

# Поиск кинотеатра по названию
def searchCinema(nameCinema):
    itemCinema = cinema.find_one({'Name': nameCinema})
    return itemCinema

# Поиск фильма по его названию
def searchFilm(nameFilm):
    itemFilm = films.find_one({'Title': nameFilm})
    return itemFilm

# Поиск актёров, снимавшихся в фильме
def searchActorFilms(films):
    id = films.get('_id')
    return list(actors.find({'Films': id}))

# Поиск фильмов, относящихся к кинотеатру
def searchFilmsCinema(cinema):
    id = cinema.get('_id')
    return list(films.find({'Cinema': id}))

# Определение id кинотеатра по названию
def getObjIdCinema(nameCinema):
    itemCinema = searchCinema(nameCinema)
    id = ObjectId(itemCinema["_id"])
    return id

# Определение id фильма по названию
def getObjIdFilm(nameFilm):
    itemFilm = searchFilm(nameFilm)
    id = ObjectId(itemFilm["_id"])
    return id

# Определение id актёра по имени
def getObjIdActor(nameActor):
    itemActor = searchActor(nameActor)
    id = ObjectId(itemActor["_id"])
    return id
