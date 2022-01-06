from scraper_helper import run_spider
from books.spiders.book_loader import BookLoaderSpider

if __name__ == '__main__':
    run_spider(BookLoaderSpider)
