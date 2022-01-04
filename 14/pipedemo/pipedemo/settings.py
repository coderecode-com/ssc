
BOT_NAME = 'pipedemo'

SPIDER_MODULES = ['pipedemo.spiders']
NEWSPIDER_MODULE = 'pipedemo.spiders'

# ITEM_PIPELINES = {
#     'pipedemo.pipelines.EcommPipeline': 300,
# }

ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
