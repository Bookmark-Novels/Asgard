from sqlalchemy import Column, Boolean, Integer, String

from db import Model

class Site(Model):
    __tablename__ = 'bookmark_sites'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    display_name = Column(String, length=255)
    vanity_name = Column(String, length=255)
    has_premium = Column(Boolean)