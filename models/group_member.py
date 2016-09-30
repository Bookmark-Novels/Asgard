from sqlalchemy import Column, Integer

from db import Model

class GroupMember(Model):
    __tablename__ = 'bookmark_group_members'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    group_id = Column(Integer)