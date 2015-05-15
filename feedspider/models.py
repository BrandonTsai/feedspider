from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, UnicodeText, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE), client_encoding='utf-8')


def create_articals_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Sources(DeclarativeBase):

    """Sqlalchemy articals model"""
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    domain = Column('source_id', String)
    feed = Column('title', String)
    updateperiod = Column('link', String)


class Articals(DeclarativeBase):

    """Sqlalchemy articals model"""
    __tablename__ = "articals"

    id = Column(Integer, primary_key=True)
    title = Column('title', UnicodeText)
    link = Column('link', String)
    content = Column('content', UnicodeText)
