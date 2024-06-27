from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    website = Column(String(150), primary_key=True, nullable=False)
    username = Column(String(150), nullable=False)
    password = Column(String(150), nullable=False)
