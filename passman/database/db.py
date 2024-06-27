import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.entry import Base, Entry


class Database:
    DATABASE_URL = os.getenv('DATABASE_URL')

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all_entries(self):
        session = self.Session()
        users = session.query(Entry).all()
        session.close()
        return users
