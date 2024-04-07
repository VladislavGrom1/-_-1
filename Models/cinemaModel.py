from pydantic import BaseModel

class Cinema(BaseModel):
    Name: str
    CompanyOwner: str
    SubscriptionCost: int
    DateOfCreation: str