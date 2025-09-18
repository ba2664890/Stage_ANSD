import scrapy


BOT_NAME = "scrapping_immobli"

SPIDER_MODULES = ["scrapping_immobli.spiders"]
NEWSPIDER_MODULE = "scrapping_immobli.spiders"

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 1
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 8
FEED_EXPORT_ENCODING = "utf-8"
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
TELNETCONSOLE_ENABLED = False

# --- UA tournant ---
USER_AGENT_LIST = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
]

DOWNLOADER_MIDDLEWARES = {
    "scrapping_immobli.middlewares.RotateUserAgentMiddleware": 400,
}

# --- pipelines ---
ITEM_PIPELINES = {
    "scrapping_immobli.pipelines.ValidationPipeline": 100,
    "scrapping_immobli.pipelines.DuplicatesPipeline": 200,
   # "scrapping_immobli.pipelines.PostgreSQLPipeline": 300,
}



    
# --- PostgreSQL ---
DATABASE = {
    "database": "scrapy_immo",
    "user": "Cardan",          
    "password": "Fatimata05?",      
    "host": "localhost",
    "port": 5432,
}