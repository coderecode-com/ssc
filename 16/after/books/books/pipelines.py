# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3


class BooksPipeline:

    def __init__(self):
        self.con = None
        self.cur = None

    def open_spider(self, spider):
        self.con = sqlite3.connect('books.db')
        spider.logger.info('Database connected')
        self.cur = self.con.cursor()
        self.create_table()

    def process_item(self, item, spider):
        self.insert_item(item, spider)
        return item

    def close_spider(self, spider):
        self.con.close()
        spider.logger.info('Database closed')

    def create_table(self):
        sql = '''
        CREATE TABLE if not exists item (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title	    TEXT,
            available	INTEGER,
            price	    NUMERIC,
            currency	TEXT
        );
        '''
        self.cur.execute(sql)

    def insert_item(self, item, spider):
        if not self.cur:
            spider.logger.warning('Database NOT open')
            return
        # sql = 'insert into table_name (col1, col2) values (?,?)'
        sql = '''
        insert into item (
              title ,  
              available ,  
              price ,  
              currency
            )
            values
            (
               ?,?,?,? 
            )
        '''
        result = self.cur.execute(sql, (
            item['title'],
            item['available'],
            item['price'],
            item['currency']
        ))
        self.con.commit()
        spider.logger.info(f'Item inserted with ID = {result.lastrowid}')

