def cinemaEntity(item) -> dict:
    return {
        "ID":str(item["_id"]),
        "Name":str(item["Name"]),
        "CompanyOwner":str(item["CompanyOwner"]),
        "SubscriptionCost":item["SubscriptionCost"],
        "DateOfCreation":str(item["DateOfCreation"]),
    }

def cinemasEntity(entity) -> list:
    return [cinemaEntity(item) for item in entity]