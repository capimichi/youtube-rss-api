from pydantic import BaseModel


class Image(BaseModel):
    url: str
    title: str
    link: str
