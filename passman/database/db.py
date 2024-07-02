from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List
from model.entry import Base, Entry


class Database:
    DATABASE_URL: str = 'mysql+mysqlconnector://root:@localhost:3306/passman'

    def __init__(self) -> None:
        self.engine = create_engine(self.DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all_entries(self) -> List[Entry]:
        session: Session = self.Session()
        entries: List[Entry] = session.query(Entry).all()
        session.close()
        return entries
