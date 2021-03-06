# -*- coding: utf-8 -*-

# Scrapy settings for feedspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'feedspider'

RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 30

SPIDER_MODULES = ['feedspider.spiders']
NEWSPIDER_MODULE = 'feedspider.spiders'


DATABASE = {
    'drivername': 'postgres',
    'host': '127.0.0.1',
    'port': '5432',
    'username': 'spider',
    'password': 'spider123',
    'database': 'scrapy'
}

ITEM_PIPELINES = ['feedspider.pipelines.FeedspiderPipeline']
