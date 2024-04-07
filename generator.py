from pymongo import MongoClient
from bson import ObjectId
import numpy as np
import pandas as pd
import re
import random
from faker import Faker
from connectMongo import connection

client, db, cinema, actors, films = connection()

# Данные для Films
filmTitles = list()
releaseDates = list()
ratingFilms = list()
genreFilms = list()
genres = ["Comedy", "Crime", "Thriller", "Action", "Adventure", "Drama", "Horror", "Animation"]
id_c = ['660d20374e2aafb4d508f5fb', '660d22f95d229501a3bc552d', '660d6a2c981f3800d88405e0', '660d6a2c981f3800d88405e1', '660d6a2c981f3800d88405e2', '660d6a2c981f3800d88405e3', '660d6a2c981f3800d88405e4']
idCinema = list()

# Данные для Actors
fake = Faker()
actorNames = list()
birthYears = list()
addInf = ["None", "Have Oscar", "Have awards"]
additionalInformation = list()
# # # # # # #
idFilms = list()
# # # # # # #

# Получение названия фильма
def getTitleFilm(film):
    film = re.split("\(", film)
    title = film[0].rstrip()
    return title

# Датасет с названиями фильмов
dfMovies = pd.read_csv('movies.csv')
titleFilms = dfMovies['title'].tolist()

# Генерация данных для Films
for i in range(1000):
    # Название
    filmTitles.append(getTitleFilm(titleFilms[i]))
    # Дата
    releaseDates.append(random.randint(1950, 2020))
    # Рейтинг
    number = random.uniform(3, 9.9)
    number = round(number, 1)
    ratingFilms.append(number)
    # Жанр
    genreFilms.append(random.choice(genres))
    # ID Cinema
    idCinema.append(ObjectId(random.choice(id_c)))


# Генерация данных для Actors
for i in range(1000):
    # Имя актёра
    actorNames.append(fake.name())
    # Год рождения
    birthYears.append(random.randint(1950,2010))
    # Дополнительная информация
    additionalInformation.append(random.choice(addInf))

for i in range(100):
    film = films.insert_one({
        "Title": filmTitles[i],
        "ReleaseDate": releaseDates[i],
        "Rating": ratingFilms[i],
        "Genre": genreFilms[i],
        "Cinema": idCinema[i] 
    })
    idFilms.append(film.inserted_id)

for i in range(100):
    actors.insert_one({
        "Name": actorNames[i],
        "BirthYear": birthYears[i],
        "AdditionalInformation": additionalInformation[i],
        "Films": idFilms[i]
    })



