from os import environ

from youtuberssapi.helper.RssHelper import RssHelper
from youtuberssapi.service.FeedService import FeedService
from youtuberssapi.service.VideoService import VideoService


class DefaultContainer:

    instance = None
    classes = {}

    def __init__(self):

        self.set('RssHelper', RssHelper(
            base_url=self.get_base_url()
        ))

        self.set('FeedService', FeedService(
            rss_helper=self.get('RssHelper'),
            base_url=self.get_base_url(),
            yt_api_key=self.get_yt_api_key()
        ))

        self.set('VideoService', VideoService())

    def get_instance(self):
        if self.instance is None:
            self.instance = DefaultContainer()
        return self.instance

    def get(self, class_name):
        if class_name in self.classes:
            return self.classes[class_name]
        return None

    def set (self, class_name, class_instance):
        self.classes[class_name] = class_instance
        return self.classes[class_name]

    def get_host(self):
        return environ.get('HOST', '0.0.0.0')

    def get_port(self):
        return int(environ.get('PORT', 8231))

    def get_base_url(self):
        return environ.get('BASE_URL', 'http://' + self.get_host() + ':' + str(self.get_port()))

    def get_yt_api_key(self):
        return environ.get('YT_API_KEY', None)