from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    website: str = Column(String(150), primary_key=True, nullable=False)
    username: str = Column(String(150), nullable=False)
    password: str = Column(String(150), nullable=False)
