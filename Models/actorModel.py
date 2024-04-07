from pydantic import BaseModel

class Actor(BaseModel):
    Name: str
    BirthYear: int
    AdditionalInformation: str
    Films: str