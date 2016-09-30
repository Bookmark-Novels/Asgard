from datetime import datetime
import traceback

from sqlalchemy import Column, Boolean, DateTime, Integer, String
from sqlalchemy.orm.exc import NoResultFound

from db import Model, session_factory

class Account(Model):
    __tablename__ = 'bookmark_accounts'

    id = Column(Integer, primary_key=True)
    email = Column(String, length=255)
    password = Column(String, length=255)
    display_name = Column(String, length=255)
    vanity_name = Column(String, length=255)
    snowflake = Column(Integer, length=255)
    verified = Column(Boolean, default=False)
    type = Column(Integer)
    patreon_id = Column(String, length=255)
    patreon_secret = Column(String, length=255)
    timezone = Column(String, length=100, default='N/A')
    created_at = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    is_auth = None

    def is_authenticated(self):
        if self.is_auth is not None:
            return self.is_auth

        with session_factory() as sess:
            try:
                sess.query(Account).filter(
                    Account.email==self.email,
                    Account.password==self.password
                ).one()

                self.is_auth = True
                return True
            except NoResultFound:
                self.is_auth = False
                return False
            except:
                traceback.print_exc()
                self.is_auth = False
                return False

    def is_anonymous(self):
        return False

    def is_active(self):
        return self.verified and self.is_active

    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def from_id(id):
        with session_factory() as session:
            try:
                account = session.query(Account).filter(
                    Account.id==id
                ).one()

                session.expunge(forum)

                return forum
            except NoResultFound:
                return None