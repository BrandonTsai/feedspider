# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Articals, db_connect, create_articals_table

class FeedspiderPipeline(object):
    """ Feedspider pipeline for storing scraped items in the database """
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates articals table.
        """
        engine = db_connect()
        create_articals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save articals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = Articals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
