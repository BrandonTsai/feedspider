# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
import json
from time import time, strftime, localtime

import scrapy

from feedspider.items import FeedspiderItem


def get_urls():
   
    t = strftime('%Y_%m%d', localtime(time()))
    sourcefile = 'feedspider/feedbot/result/%s.json' % t
    with open(sourcefile) as data_file:
        urls = json.load(data_file)
    #urls = [
    #    "http://libertytimes.feedsportal.com/c/33098/f/535603/s/45bce560/sc/23/l/0L0Staipeitimes0N0CNews0Cbiz0Carchives0C20A150C0A40C260C20A0A3616793/story01.htm",
    #    "http://libertytimes.feedsportal.com/c/33098/f/535603/s/45d26f4e/sc/28/l/0L0Staipeitimes0N0CNews0Cbiz0Carchives0C20A150C0A40C290C20A0A36170A30A/story01.htm"
    #]

    return urls


class MLStripper(HTMLParser):
    """ strip HTML tags """
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


class TextspiderSpider(scrapy.Spider):
    name = "textspider"
    allowed_domains = ["text.com"]
    start_urls = get_urls()

    def parse(self, response):

        item = FeedspiderItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()[0]
        item['link'] = response.xpath('/html/head//meta[@property="og:url"]/@content').extract()[0]
        #item['content'] = response.xpath('//div[@class="text"]').extract()[0]
        c = MLStripper()
        c.feed(response.xpath('//div[@class="text"]').extract()[0])
        item['content'] = c.get_data()

        print "--- ", item['title'], " ---"
        return item

