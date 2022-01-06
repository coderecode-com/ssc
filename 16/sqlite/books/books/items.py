# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join
from price_parser import Price
from w3lib.html import remove_tags


def get_price(price_raw):
    price_object = Price.fromstring(price_raw)
    price = price_object.amount_float
    return price


def get_currency(price_raw):
    price_object = Price.fromstring(price_raw)
    currency = price_object.currency
    return currency


def stock_to_bool(in_stock):
    if in_stock and 'in stock' in in_stock.lower():
        return True
    else:
        return False


class BooksItem(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
    available = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, stock_to_bool),
        output_processor=TakeFirst()
    )
    currency = scrapy.Field(
        input_processor=MapCompose(get_currency),
        output_processor=TakeFirst()
    )
