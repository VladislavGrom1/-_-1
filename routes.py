from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from scripts import getObjIdCinema, getObjIdFilm, getObjIdActor
from Entity.films import filmEntity,filmsEntity
from Entity.actors import actorEntity,actorsEntity
from Entity.cinemas import cinemaEntity, cinemasEntity
from Models.filmModel import Film
from Models.cinemaModel import Cinema
from Models.actorModel import Actor
from connectMongo import connection
 
client, db, cinema, actors, films = connection()
user = APIRouter()

# Вывод фильмов
@user.get("/films")
async def search_all_films():
    return filmsEntity(films.find())

# Вывод актёров
@user.get("/actors")
async def search_all_actors():
    return actorsEntity(actors.find()) 

# Вывод кинотеатров
@user.get("/cinemas")
async def search_all_cinemas():
    return cinemasEntity(cinema.find())

# Добавление фильма
@user.post("/insert_film")
async def insert_film(film: Film):
    idCinema = getObjIdCinema(film.Cinema)
    film.Cinema = idCinema
    films.insert_one(dict(film))
    return filmsEntity(films.find())

# Добавление актёра
@user.post("/insert_actor")
async def insert_actor(actor: Actor):
    idFilm = getObjIdFilm(actor.Films)
    actor.Films = idFilm
    actors.insert_one(dict(actor))
    return actorsEntity(actors.find())

# Добавление кинотеатра
@user.post("/insert_cinema")
async def insert_cinema(cinemaM: Cinema):
    cinema.insert_one(dict(cinemaM))
    return cinemasEntity(cinema.find())

# Обновление данных фильма
@user.put('/update_film/{Title}')
async def update_film(Title, film: Film):
    # Поиск id фильма по названию
    idFilm = getObjIdFilm(Title)
    # Поиск id кинотеатра по названию
    idCinema = getObjIdCinema(film.Cinema)
    film.Cinema = idCinema
    # Поиск и обновление по ID
    films.find_one_and_update({"_id":idFilm}, {"$set": dict(film)})
    return filmEntity(films.find_one({"_id": idFilm}))

# Обновление данных актёра
@user.put('/update_actor/{Name}')
async def update_film(Name, actor: Actor):
    # Поиск id актёра по имени
    idActor = getObjIdActor(Name)
    # Поиск id фильма по названию
    idFilm = getObjIdFilm(actor.Films)
    actor.Films = idFilm
    # Поиск и обновление по ID
    actors.find_one_and_update({"_id":idActor}, {"$set": dict(actor)})
    return actorEntity(actors.find_one({"_id": idActor}))

# Обновление данных кинотеатра
@user.put('/update_cinema/{Name}')
async def update_cinema(Name, cinemaM: Cinema):
    # Поиск id кинотеатра по имени
    idCinema = getObjIdCinema(Name)
    # Поиск и обновление по ID
    cinema.find_one_and_update({"_id":idCinema}, {"$set": dict(cinemaM)})
    return cinemaEntity(cinema.find_one({"_id": idCinema}))

# Удаление фильма
@user.delete('/delete_film/{Title}')
async def delete_film(Title):
    # Поиск id фильма по имени
    idFilm = getObjIdFilm(Title)
    return filmEntity(films.find_one_and_delete({"_id": idFilm}))

# Удаление актёра
@user.delete('/delete_actor/{Name}')
async def delete_actor(Name):
    # Поиск id актёра по имени
    idActor = getObjIdActor(Name)
    return actorEntity(actors.find_one_and_delete({"_id": idActor}))

# Удаление кинотеатра
@user.delete('/delete_cinema/{Name}')
async def delete_cinema(Name):
    # Поиск id кинотеатра по имени
    idCinema = getObjIdCinema(Name)
    return cinemaEntity(cinema.find_one_and_delete({'_id': idCinema}))
