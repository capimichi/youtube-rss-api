from fastapi import FastAPI

from youtuberssapi.container.DefaultContainer import DefaultContainer
from youtuberssapi.service.FeedService import FeedService

default_container = DefaultContainer()
app = FastAPI()

@app.get("/feed")
async def get_feed(url: str):
    feed_service: FeedService = default_container.get('FeedService')
    return feed_service.getFeed(url)

@app.get("/video")
async def get_video(id: str):
    # Here you can add the logic to handle the video ID
    return {"message": f"Video with id {id}"}