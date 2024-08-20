import sqlalchemy

from app import db

class Book(db.Base):
    __table__ = "book"


