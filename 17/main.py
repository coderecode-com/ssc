from scrapy.crawler import CrawlerProcess
from data.spiders.books import BooksSpider
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(BooksSpider)
process.start()