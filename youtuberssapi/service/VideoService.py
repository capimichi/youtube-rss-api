import os

import requests
import youtube_dl

from youtuberssapi.helper.RssHelper import RssHelper
from youtuberssapi.model.Channel import Channel
from youtuberssapi.model.Image import Image
from youtuberssapi.model.Item import Item
from youtuberssapi.model.Owner import Owner
from youtuberssapi.model.Rss import Rss

from bs4 import BeautifulSoup


class VideoService:

    def getVideoMp3Content(self, video_id):

        file_name = video_id + '.mp3'
        ytdl = youtube_dl.YoutubeDL({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': file_name
        })
        info_dict = ytdl.extract_info(video_id, download=True)

        with open(file_name, 'rb') as audio_file:
            content = audio_file.read()

        # remove the downloaded file
        os.remove(file_name)

        return content
