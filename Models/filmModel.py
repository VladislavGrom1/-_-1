from pydantic import BaseModel

class Film(BaseModel):
    Title: str
    ReleaseDate: int
    Rating: float
    Genre: str
    Cinema: str