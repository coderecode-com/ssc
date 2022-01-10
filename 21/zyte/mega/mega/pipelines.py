# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MegaPipeline:
    def __init__(self):
        self.asin_seen = []

    def process_item(self, item, spider):
        asin = ItemAdapter(item).get('asin')
        if asin and asin in self.asin_seen:
            raise DropItem("Duplicate ASIN found")
        self.asin_seen.append(asin)
        return item
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MegaPipeline:
    def __init__(self):
        self.asin_seen = []

    def process_item(self, item, spider):
        asin = ItemAdapter(item).get('asin')
        if asin and asin in self.asin_seen:
            raise DropItem(f'Duplicate Item: {asin}')
        self.asin_seen.append(asin)
        return item
