#!/usr/bin/python

from sys import argv
import json
from time import time, strftime, localtime

import feedparser



def get_rss_source_list(sourcefile):
    #sourcefile = 'source.json'
    with open(sourcefile) as infile:
        source = json.load(infile)

    return source

def get_feed_links(source_list):

    L = []
    for source in source_list:
        d = feedparser.parse(source)
        for entry in d['entries']:
            #print "----------------------"
            #for k, v in entry.items():
            #    print k, " >> ", v
            #L.append(entry['feedburner_origlink'])
            L.append(entry['id'])
    
    return L


if __name__ == '__main__':

    source_list = get_rss_source_list(argv[1])
    L = get_feed_links(source_list)

    t = strftime('%Y_%m%d', localtime(time()))
    targetfile = './result/%s.json' % t
    with open(targetfile, 'w') as outfile:
        json.dump(L, outfile)


