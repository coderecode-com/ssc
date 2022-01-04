# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem


class AmazonPipeline:
    def open_spider(self, spider):
        spider.logger.info('Opening spider')

    def process_item(self, item, spider):
        if 'Apple' in item.get('Product'):
            raise DropItem('Dropping Apple Laptops')
        spider.logger.info(f'Processing item: {type(item)}')
        return item

    def close_spider(self, spider):
        spider.logger.info('Closing spider')


class QuotesPipeline:
    stop_words = [
        'hate', 'mad'
    ]

    def open_spider(self, spider):
        spider.logger.info('Opening spider')

    def process_item(self, item, spider):
        text = item.get('Quote')
        for word in self.stop_words:
            if word in text.lower():
                #  raise DropItem("Stop word found.")
                item['Quote'] = text.replace(word, '*' * len(word))
        return item

    def close_spider(self, spider):
        spider.logger.info('Closing spider')
