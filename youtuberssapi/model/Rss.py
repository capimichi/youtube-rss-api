from pydantic import BaseModel
from typing import Optional, List

from youtuberssapi.model.Channel import Channel


class Rss(BaseModel):
    channel: Channel
