# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MediaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    BookTitle = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    image_urls = scrapy.Field()
    images= scrapy.Field()
