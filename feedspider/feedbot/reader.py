#!/usr/bin/python

from sys import argv
import json
from time import time, strftime, localtime
from os import listdir
from os.path import isfile, join

import feedparser


def get_rss_source_list(source_folder):
    # get source file list in source folder.
    source_files = [join(source_folder, f) for f in listdir(
        source_folder) if isfile(join(source_folder, f))]

    all_source = []
    for sf in source_files:
        with open(sf) as infile:
            source = json.load(infile)
        all_source.extend(source)
    return all_source


def get_feed_links(source_list):

    L = []
    for source in source_list:
        d = feedparser.parse(source)
        for entry in d['entries']:
            L.append(entry['id'])

    return L


if __name__ == '__main__':

    source_dir = "source/"
    S = get_rss_source_list(source_dir)
    L = get_feed_links(S)

    t = strftime('%Y_%m%d', localtime(time()))
    targetfile = './result/%s.json' % t
    with open(targetfile, 'w') as outfile:
        json.dump(L, outfile)
