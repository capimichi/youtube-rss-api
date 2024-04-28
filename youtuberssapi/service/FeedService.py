import requests
import youtube_dl

from youtuberssapi.helper.RssHelper import RssHelper
from youtuberssapi.model.Channel import Channel
from youtuberssapi.model.Image import Image
from youtuberssapi.model.Item import Item
from youtuberssapi.model.Owner import Owner
from youtuberssapi.model.Rss import Rss

from bs4 import BeautifulSoup


class FeedService:

    base_url = None

    rss_helper: RssHelper = None

    def __init__(
            self,
            rss_helper: RssHelper,
            base_url: str
    ):
        self.rss_helper = rss_helper
        self.base_url = base_url

    def getFeed(self,
                youtube_url,
                page: int = 1,
                per_page: int = 10
                ):

        ytdl = youtube_dl.YoutubeDL({
            # 'ignoreerrors': True,
            # 'quiet': True,
            # 'no_warnings': True,
            'dump_single_json': True,
        })
        info_dict = ytdl.extract_info(youtube_url, download=False, process=False)

        page_content_res = requests.get(youtube_url).content
        page_content = page_content_res.decode('utf-8')
        bs = BeautifulSoup(page_content, 'html.parser')

        # get og:image
        image_url = bs.find('meta', property='og:image')['content']

        title = info_dict['title']

        # video_ids = [video['id'] for video in info_dict['entries']]
        video_ids = ["8yv2qfQhW68"]

        # slice the list of video ids
        start = (page - 1) * per_page
        end = start + per_page
        video_ids = video_ids[start:end]

        items = []
        for video_id in video_ids:
            video_data = ytdl.extract_info(video_id, download=True, process=False)

            item = Item(
                title=video_data['title'],
                description=video_data['description'],
                pubDate=video_data['upload_date'],
                episodeType='full',
                author='la7',
                subtitle=None,
                summary=video_data['description'],
                encoded='<p>' + video_data['description'] + '</p>',
                duration=video_data['duration'],
                guid=video_data['id'],
                enclosure=self.base_url + '/video/' + video_data['id']
            )
            items.append(item)

        channel = Channel(
            title=title,
            link=info_dict['webpage_url'],
            language='it',
            copyright='© la7',
            description=info_dict['description'],
            image=Image(url=image_url, title=title, link=image_url),
            explicit='no',
            type='episodic',
            subtitle=None,
            author='la7',
            summary=info_dict['description'],
            encoded='<p>' + info_dict['description'] + '</p>',
            owner=Owner(name='la7', email=''),
            image_href=image_url,
            category=['Society & Culture', 'News'],
            items=items
        )

        rss = Rss(channel=channel)

        xml_data = self.rss_helper.rss_to_xml(rss)

        return xml_data

    def set_base_url(self, base_url):
        self.base_url = base_url
        return self.base_url