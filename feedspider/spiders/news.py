# -*- coding: utf-8 -*-

import json
import lxml.html
from time import time, strftime, localtime
import os.path

import scrapy

from feedspider.items import FeedspiderItem


def get_urls():

    t = strftime('%Y_%m%d', localtime(time()))
    sourcefile = 'feedspider/feedbot/result/%s.json' % t
    if os.path.isfile(sourcefile):
        with open(sourcefile) as data_file:
            urls = json.load(data_file)
    else:
        urls = []
    return urls


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["basic.com"]
    start_urls = get_urls()

    def parse(self, response):
        item = FeedspiderItem()
        item['title'] = ''.join(response.xpath('//title/text()').extract())
        item['link'] = response.url
        contentList = response.xpath('//p/text() | //p/a/text()').extract()
        item['content'] = ''.join(contentList)
        # print "\n~~", item
        return item
