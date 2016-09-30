from sqlalchemy import Column, Boolean, Integer, String

from db import Model

class Story(Model):
    __tablename__ = 'bookmark_stories'

    id = Column(Integer, primary_key=True)
    display_name = Column(String, length=255)
    vanity_name = Column(String, length=255)
    cover_url = Column(Strng, 1000)
    site_id = Column(Integer)
    author = Column(String, 255)
    source_url = Column(String, 1000)
    ongoing = Column(Boolean)