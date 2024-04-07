def actorEntity(item) -> dict:
    return {
        "ID":str(item["_id"]),
        "Name":str(item["Name"]),
        "BirthYear":item["BirthYear"],
        "AdditionalInformation":item["AdditionalInformation"],
        "Films":str(item["Films"])
    }

def actorsEntity(entity) -> list:
    return [actorEntity(item) for item in entity]