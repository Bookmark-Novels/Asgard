from datetime import datetime

from sqlalchemy import Column, Boolean, DateTime, Integer, String

from db import Model

class ChapterContent(Model):
    __tablename__ = 'bookmark_chapter_content'

    id = Column(Integer, primary_key=True)
    chapter_id = Column(Integer)
    editor_id = Column(Integer)
    revision = Column(Integer, default=1)
    revision_note = Column(String, length=25000)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    site_id = Column(Integer)