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

        podcast_content = f"""<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0" xmlns:spotify="https://www.spotify.com/ns/rss" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
<channel>
<title>Otto e mezzo </title>
<link>https://www.la7.it/otto-e-mezzo</link>
<language>it</language>
<copyright>© la7</copyright>
<itunes:subtitle/>
<itunes:author>la7</itunes:author>
<itunes:summary>
<![CDATA[ Ascolta il racconto dell'attualit&#xE0; con Lilli Gruber e i suoi ospiti. Tutti i giorni le puntate integrali di Otto e Mezzo. ]]>
</itunes:summary>
<description>
<![CDATA[ Ascolta il racconto dell'attualit&#xE0; con Lilli Gruber e i suoi ospiti. Tutti i giorni le puntate integrali di Otto e Mezzo. ]]>
</description>
<itunes:image href="https://www.la7.it/sites/default/files/8emezzo_podcast_cover_0.jpg"/>
<image>
<url>https://www.la7.it/sites/default/files/8emezzo_podcast_cover_0.jpg</url>
<title>Otto e mezzo </title>
<link>https://www.la7.it/otto-e-mezzo</link>
</image>
<itunes:owner>
<itunes:name>la7</itunes:name>
<itunes:email>podcast@la7.it</itunes:email>
</itunes:owner>
<itunes:category text="Society & Culture"/>
<itunes:category text="News"/>
<itunes:explicit>no</itunes:explicit>
<item>
<guid isPermaLink="false">1988158226</guid>
<title>Otto e Mezzo</title>
<itunes:title>Otto e Mezzo</itunes:title>
<description>
<![CDATA[ Ospiti di Lilli Gruber: Franco Bernab&#xE8;, Massimo Giannini, Lucio Caracciolo, Nadia Urbinati ]]>
</description>
<itunes:summary>
<![CDATA[ Ospiti di Lilli Gruber: Franco Bernab&#xE8;, Massimo Giannini, Lucio Caracciolo, Nadia Urbinati ]]>
</itunes:summary>
<itunes:author>la7</itunes:author>
<itunes:image href="https://www.la7.it/sites/default/files/8emezzo_podcast_cover_0.jpg"/>
<media:content url="https://www.la7.it/sites/default/files/8emezzo_podcast_cover_0.jpg" type="image/jpeg"/>
<category>News</category>
<itunes:category text="News"/>
<category>Society & Culture</category>
<itunes:category text="Society &amp; Culture"/>
<itunes:keywords>News Society & Culture</itunes:keywords>
<enclosure url="https://limone.iltrovatore.it/audio.mp3?source_r=itunes&fn=podcast-otto-e-mezzo-474513.mp3&mp3l=1979&mp3pid=otto-e-mezzo" length="1979" type="audio/mpeg"/>
<media:content url="https://limone.iltrovatore.it/audio.mp3?source_r=itunes&fn=podcast-otto-e-mezzo-474513.mp3&mp3l=1979&mp3pid=otto-e-mezzo" type="audio/mpeg">
<media:player url="https://www.la7.it/embed/podcas/474513"/>
</media:content>
<itunes:duration>1979</itunes:duration>
<pubDate>Fri, 03 Mar 2023 20:33:30 +0100</pubDate>
<itunes:explicit>no</itunes:explicit>
</item>
</channel>
</rss>"""

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