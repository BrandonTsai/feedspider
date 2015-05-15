#!/bin/bash

LOG_FILE=/var/log/feedspider.log
exec 3>&1 1>>${LOG_FILE} 2>&1

## get today's feeds
pushd ./feedspider/feedbot/
./reader.py
popd

## run spider.
scrapy crawl news &
