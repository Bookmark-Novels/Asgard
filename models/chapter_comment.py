from datetime import datetime

from sqlalchemy import Column, Boolean, DateTime, Integer, String

from db import Model

class ChapterComment(Model):
    __tablename__ = 'bookmark_chapter_comments'

    id = Column(Integer, primary_key=True)
    chapter_id = Column(Integer)
    author_id = Column(Integer)
    last_updated = Column(DateTime)
    timestamp = Column(DateTime)
    pending_verification = Column(Boolean, default=False)
    comment = Column(String, length=40000)