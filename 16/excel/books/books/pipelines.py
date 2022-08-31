# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import xlsxwriter


class ExcelOutputPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            excel_file=crawler.settings.get('EXCEL_FILE')
        )

    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.workbook = None
        self.worksheet = None
        self.cell_format = None
        self.heading_format = None
        self.current_row_index = 0  # row index 0 in python is row 1 in Excel

    def open_spider(self, spider):
        if not self.excel_file:
            spider.logger.error('EXCEL_FILE not found in settings.')
            return
        self.workbook = xlsxwriter.Workbook(self.excel_file)
        self.worksheet = self.workbook.add_worksheet()
        self.heading_format = self.workbook.add_format()
        self.heading_format.set_bold()
        self.heading_format.set_border(1)

        self.cell_format = self.workbook.add_format()
        self.cell_format.set_border(1)
        self.cell_format.set_border(1)

    def process_item(self, item, spider):
        self.insert_item(item, spider)
        return item

    def close_spider(self, spider):
        self.workbook.close()

    def create_header(self):
        self.current_row_index += 1

    def insert_item(self, item, spider):
        adapter = ItemAdapter(item)
        d = adapter.asdict()

        if self.current_row_index == 0:  # Write Header
            fmt = self.heading_format
            for column, value in enumerate(d.keys()):
                self.worksheet.write(self.current_row_index, column, value, fmt)

        data = d.values()
        fmt = self.cell_format

        for column, value in enumerate(data):
            self.worksheet.write(self.current_row_index+1, column, value, fmt)

        self.current_row_index += 1
