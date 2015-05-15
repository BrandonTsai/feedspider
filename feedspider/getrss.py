#!/usr/bin/python

from sys import argv
import json
from time import time, strftime, localtime

import feedparser

from models import db_connect


def get_rss_source_list(sourcefile):
    with open(sourcefile) as infile:
        source = json.load(infile)

    return source


def get_feed_links(source_list):

    L = []
    for source in source_list:
        d = feedparser.parse(source)
        for entry in d['entries']:
            L.append(entry['id'])

    return L


def remove_depluciation(all_links):

    engine = db_connect()
    connection = engine.connect()
    dup_links = connection.execute(
        "select link from articals where link in %s",
        [(tuple(all_links),)]).fetchall()
    connection.close()
    R = all_links
    if not dup_links:
        for l in dup_links:
            R.remove(l)
    return R

if __name__ == '__main__':

    source_list = get_rss_source_list(argv[1])
    F = get_feed_links(source_list)
    L = remove_depluciation(F)
    t = strftime('%Y_%m%d', localtime(time()))
    targetfile = 'feedbot/result/%s.json' % t
    with open(targetfile, 'w') as outfile:
        json.dump(L, outfile)
