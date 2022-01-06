
BOT_NAME = 'books'
SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'
ITEM_PIPELINES = {
   'books.pipelines.BooksPipeline': 300,
}
ROBOTSTXT_OBEY = True
