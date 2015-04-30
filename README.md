# Feedspider

A Scrapy spider that extract the content from RSS Feed.

pip Requirements:
- postgreSQL
- sqlalchemy
- scrapy
- feedparser

## get RSS Entries every hour.

### get RSS source_list

return a list off RSS source_list from json

(future)
store source list in table rss_source

(future)
select source according the sy_updateperiod is daily or hourly

### get feeds
if entry.link in table articles:
  ignore
else:
  insert (title, publishd_date, link, summary) into table articles:



## run Scrapy everyday.

get entry link from table articles where content is null.

for each link, run spider to extract main content.
