from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    title: str
    description: str
    pubDate: str
    episodeType: str
    author: str
    subtitle: Optional[str]
    summary: str
    encoded: str
    duration: int
    guid: str
    enclosure: str
