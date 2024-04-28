from pydantic import BaseModel


class Owner(BaseModel):
    name: str
    email: str
