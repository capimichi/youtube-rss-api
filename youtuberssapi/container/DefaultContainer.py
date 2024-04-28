from youtuberssapi.service.FeedService import FeedService


class DefaultContainer:

    instance = None
    classes = {}

    def __init__(self):
        self.set('FeedService', FeedService())

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