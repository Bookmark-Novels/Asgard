from datetime import datetime

from sqlalchemy import Column, BigInteger, Boolean, DateTime, Integer, String

from db import Model

class Chapter(Model):
    __tablename__ = 'bookmark_chapters'

    id = Column(Integer, primary_key=True)
    story_id = Column(Integer)
    volume_id = Column(Integer)
    author_id = Column(Integer)
    display_name = Column(String, length=255)
    vanity_name = Column(String, length=255)
    is_released = Column(Boolean)
    release_at = Column(DateTime, default=datetime.utcnow)
    allow_patreon = Column(Boolean)
    minimum_pledge = Column(Integer)
    summary = Column(String, length=25000)
    teaser = Column(String, length=25000)
    views = Column(BigInteger, default=0)
    allow_comments = Column(Boolean, default=True)
    require_comment_verification = Column(Boolean, default=False)
    site_id = Column(Integer)