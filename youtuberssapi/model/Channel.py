from typing import List, Optional
from pydantic import BaseModel
from youtuberssapi.model.Image import Image
from youtuberssapi.model.Item import Item
from youtuberssapi.model.Owner import Owner


class Channel(BaseModel):
    link: str
    title: str
    language: str
    copyright: str
    description: str
    image: Image
    explicit: str
    type: str
    subtitle: Optional[str]
    author: str
    summary: str
    encoded: str
    owner: Owner
    image_href: str
    category: List[str]
    items: List[Item]
