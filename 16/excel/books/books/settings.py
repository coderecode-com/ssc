BOT_NAME = 'books'
SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'books.pipelines.ExcelOutputPipeline': 300,
}
EXCEL_FILE = 'output.xlsx'