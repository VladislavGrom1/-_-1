def filmEntity(item) -> dict:
    return {
        "ID":str(item["_id"]),
        "Title":str(item["Title"]),
        "ReleaseDate":item["ReleaseDate"],
        "Rating":item["Rating"],
        "Genre":str(item["Genre"]),
        "Cinema":str(item["Cinema"])
    }

def filmsEntity(entity) -> list:
    return [filmEntity(item) for item in entity]