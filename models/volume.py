from sqlalchemy import Column, Boolean, Integer, String

from db import Model

class Volume(Model):
    __tablename__ = 'bookmark_volumes'

    id = Column(Integer, primary_key=True)
    display_name = Column(String, length=255)
    vanity_name = Column(String, length=255)
    cover_url = Column(String, length=1000)
    story_id = Column(Integer)
    site_id = Column(Integer)