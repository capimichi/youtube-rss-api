from os import environ

from fastapi import FastAPI

from youtuberssapi.container.DefaultContainer import DefaultContainer
from youtuberssapi.service.FeedService import FeedService
import youtube_dl
from fastapi.responses import Response

from youtuberssapi.service.VideoService import VideoService

default_container = DefaultContainer()
app = FastAPI()


@app.get("/feed")
async def get_feed(url: str, page: int = 1, per_page: int = 10):
    feed_service: FeedService = default_container.get('FeedService')
    feed_xml_data = feed_service.getFeed(url, page=page, per_page=per_page)
    return Response(content=feed_xml_data, media_type="application/xml")

@app.get("/video/{id}")
async def get_video(id: str):
    video_service: VideoService = default_container.get('VideoService')
    audio_content = video_service.getVideoMp3Content(id)
    return Response(content=audio_content, media_type="audio/mpeg")

# start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=default_container.get_host(), port=default_container.get_port())