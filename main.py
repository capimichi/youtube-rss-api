from os import environ

from fastapi import FastAPI
import uvicorn
from youtuberssapi.container.DefaultContainer import DefaultContainer
from youtuberssapi.service.FeedService import FeedService
import youtube_dl
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

from youtuberssapi.service.VideoService import VideoService

default_container = DefaultContainer()

app = FastAPI(docs_url="/swagger", servers=[{"url": default_container.get_base_url()}])
router = APIRouter()


app.mount("/docs/", StaticFiles(directory="./docusaurus/build", html=True), name="static")

@router.get("/feed",tags=["Feed"])
async def get_feed(channel_id: str, page: int = 1, per_page: int = 10):
    feed_service: FeedService = default_container.get('FeedService')
    feed_xml_data = feed_service.getFeed(channel_id, page=page, per_page=per_page)
    return Response(content=feed_xml_data, media_type="application/xml")

@router.get("/video/{id}",tags=["Video"])
async def get_video(id: str):
    video_service: VideoService = default_container.get('VideoService')
    audio_content = video_service.getVideoMp3Content(id)
    return Response(content=audio_content, media_type="audio/mpeg")

app.include_router(router, prefix="/api")

# start the server
if __name__ == "__main__":
    uvicorn.run(app, host=default_container.get_host(), port=default_container.get_port())