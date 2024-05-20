import json
import os

import requests
import youtube_dl

from youtuberssapi.helper.RssHelper import RssHelper
from youtuberssapi.model.Channel import Channel
from youtuberssapi.model.Image import Image
from youtuberssapi.model.Item import Item
from youtuberssapi.model.Owner import Owner
from youtuberssapi.model.Rss import Rss

import re

from bs4 import BeautifulSoup


class FeedService:

    base_url = None
    yt_api_key = None

    rss_helper: RssHelper = None

    def __init__(
            self,
            rss_helper: RssHelper,
            base_url: str,
            yt_api_key: str
    ):
        self.rss_helper = rss_helper
        self.base_url = base_url
        self.yt_api_key = yt_api_key

    def getFeed(self,
                channel_id: str,
                page: int = 1,
                per_page: int = 10
                ):


        video_ids = self.get_video_ids(channel_id, page, per_page)

        items = []

        channel_data = self.get_channel_data(channel_id)

        podcast_content = self.rss_helper.get_podcast_content(channel_id, channel_data)

        return podcast_content

    def set_base_url(self, base_url):
        self.base_url = base_url
        return self.base_url

    def get_video_ids(self, channel_id, page, per_page):
        api_key = self.yt_api_key
        url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20'
        response = requests.get(url)
        json_data = json.loads(response.text)

        video_ids = []
        for item in json_data['items']:
            id_data = item['id']
            if(id_data['kind'] == 'youtube#video'):
                video_ids.append(item['id']['videoId'])

        return video_ids

    def get_channel_data(self, channel_id):
        api_key = self.yt_api_key
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}'
        response = requests.get(url)
        json_data = json.loads(response.text)

        return json_data['items'][0]['snippet']