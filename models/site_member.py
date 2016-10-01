from sqlalchemy import Column, Integer

from db import Model

class SiteMember(Model):
    __tablename__ = 'bookmark_site_members'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer)
    account_id = Column(Integer)