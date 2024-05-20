import xml.etree.cElementTree as ET
import cgi

class RssHelper:

    def rss_to_xml(self, rss):

        namespaces = {
            "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
            "xmlns:googleplay": "http://www.google.com/schemas/play-podcasts/1.0",
            "xmlns:atom": "http://www.w3.org/2005/Atom",
            "xmlns:media": "http://search.yahoo.com/mrss/",
            "xmlns:content": "http://purl.org/rss/1.0/modules/content/",
        }
        root = ET.Element("rss", attrib=namespaces, version="2.0")
        # rest of the code

        channel = ET.SubElement(root, "channel")
        title = ET.SubElement(channel, "title")
        title.text = rss.channel.title
        link = ET.SubElement(channel, "link")
        link.text = rss.channel.link
        language = ET.SubElement(channel, "language")
        language.text = rss.channel.language
        copyright = ET.SubElement(channel, "copyright")
        copyright.text = rss.channel.copyright
        description = ET.SubElement(channel, "description")
        description.text = rss.channel.description
        image = ET.SubElement(channel, "image")
        url = ET.SubElement(image, "url")
        url.text = rss.channel.image.url
        title = ET.SubElement(image, "title")
        title.text = rss.channel.image.title
        link = ET.SubElement(image, "link")
        link.text = rss.channel.image.link
        explicit = ET.SubElement(channel, "itunes:explicit")
        explicit.text = rss.channel.explicit
        type = ET.SubElement(channel, "itunes:type")
        type.text = rss.channel.type
        subtitle = ET.SubElement(channel, "itunes:subtitle")
        subtitle.text = rss.channel.subtitle
        author = ET.SubElement(channel, "itunes:author")
        author.text = rss.channel.author
        summary = ET.SubElement(channel, "itunes:summary")
        summary.text = rss.channel.summary
        owner = ET.SubElement(channel, "itunes:owner")
        name = ET.SubElement(owner, "itunes:name")
        name.text = rss.channel.owner.name
        email = ET.SubElement(owner, "itunes:email")
        email.text = rss.channel.owner.email
        image_href = ET.SubElement(channel, "itunes:image")
        image_href.text = rss.channel.image_href
        for category_name in rss.channel.category:
            category = ET.SubElement(channel, "itunes:category")
            category.text = category_name
        items = ET.SubElement(channel, "items")

        for item in rss.channel.items:
            item_element = ET.SubElement(items, "item")
            title = ET.SubElement(item_element, "title")
            title.text = item.title
            description = ET.SubElement(item_element, "description")
            description.text = item.description
            pubDate = ET.SubElement(item_element, "pubDate")
            pubDate.text = item.pubDate
            episodeType = ET.SubElement(item_element, "itunes:episodeType")
            episodeType.text = item.episodeType
            author = ET.SubElement(item_element, "itunes:author")
            author.text = item.author
            summary = ET.SubElement(item_element, "itunes:summary")
            summary.text = item.summary
            encoded = ET.SubElement(item_element, "itunes:encoded")
            encoded.text = item.encoded
            duration = ET.SubElement(item_element, "itunes:duration")
            duration.text = str(item.duration)
            guid = ET.SubElement(item_element, "guid")
            guid.text = item.guid
            enclosure = ET.SubElement(item_element, "enclosure")
            enclosure.set("url", item.enclosure)
            enclosure.set("length", "0")
            enclosure.set("type", "audio/mpeg")

        return ET.tostring(root)

    def get_podcast_content(self, channel_id, channel_data, videos):

        items = ""
        for video in videos:
            title = video['snippet']['title']
            title = cgi.escape(title)
            thumbnail = video['snippet']['thumbnails']['medium']['url']
            item = f"""<item>
        <guid isPermaLink="false">1988158226</guid>
        <title>{title}</title>
        <itunes:title>{title}</itunes:title>
        <description>
        <![CDATA[ {title} ]]>
        </description>
        <itunes:summary>
        <![CDATA[ {title} ]]>
        </itunes:summary>
        <itunes:author>la7</itunes:author>
        <itunes:image href="{thumbnail}"/>
        <media:content url="{thumbnail}" type="image/jpeg"/>
        <category>News</category>
        <itunes:category text="News"/>
        <category>Society &amp; Culture</category>
        <itunes:category text="Society &amp; Culture"/>
        <itunes:keywords>News Society &amp; Culture</itunes:keywords>
        <enclosure url="https://limone.iltrovatore.it/audio.mp3?source_r=itunes&amp;fn=podcast-otto-e-mezzo-474513.mp3&amp;mp3l=1979&amp;mp3pid=otto-e-mezzo" type="audio/mpeg"/>
        <media:content url="https://limone.iltrovatore.it/audio.mp3?source_r=itunes&amp;fn=podcast-otto-e-mezzo-474513.mp3&amp;mp3l=1979&amp;mp3pid=otto-e-mezzo" type="audio/mpeg">
        <media:player url="https://www.la7.it/embed/podcas/474513"/>
        </media:content>
        <itunes:duration>1979</itunes:duration>
        <pubDate>Fri, 03 Mar 2023 20:33:30 +0100</pubDate>
        <itunes:explicit>no</itunes:explicit>
        </item>"""
            items += item

        title = channel_data['title']
        link = "https://www.youtube.com/" + channel_data['customUrl']
        thumbnail = channel_data['thumbnails']['medium']['url']

        podcast_content = f"""<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0" xmlns:spotify="https://www.spotify.com/ns/rss" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
        <channel>
        <title>{title}</title>
        <link>{link}</link>
        <language>it</language>
        <copyright>youtube</copyright>
        <itunes:subtitle/>
        <itunes:author>youtube</itunes:author>
        <itunes:summary>
        <![CDATA[ {title} ]]>
        </itunes:summary>
        <description>
        <![CDATA[ {title} ]]>
        </description>
        <itunes:image href="{thumbnail}"/>
        <image>
        <url>{thumbnail}</url>
        <title>{title}</title>
        <link>{link}</link>
        </image>
        <itunes:owner>
        <itunes:name>youtube</itunes:name>
        <itunes:email>info@youtube.com</itunes:email>
        </itunes:owner>
        <itunes:category text="Society &amp; Culture"/>
        <itunes:category text="News"/>
        <itunes:explicit>no</itunes:explicit>
        {items}
        </channel>
        </rss>"""

        return podcast_content
