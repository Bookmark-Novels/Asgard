from sqlalchemy import Column, Boolean, Integer, String

from db import Model

class Group(Model):
    __tablename__ = 'bookmark_groups'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer)
    display_name = Column(String, length=255)
    vanity_name = Column(String, length=255)
    can_admin = Column(Boolean)
    can_author = Column(Boolean)
    can_edit = Column(Boolean)
    can_release = Column(Boolean)
    can_moderate = Column(Boolean)