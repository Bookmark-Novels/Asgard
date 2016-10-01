from sqlalchemy import Column, Integer, String

from db import Model

class RevisionDIff(Model):
    __tablename__ = 'bookmark_revision_diffs'

    id = Column(Integer, primary_key=True)
    from_revision = Column(Integer)
    to_revision = Column(Integer)
    diff = (String)