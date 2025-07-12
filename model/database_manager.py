from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL, DATABASE_PATH
import os

Base = declarative_base()
Engine = create_engine(DATABASE_URL)

class DatabaseManager:
    def __init__(self, db_url=DATABASE_URL):
        self.session = sessionmaker(bind=Engine)
        self._create_database_dir()

    def _create_database_dir(self):
        if not os.path.exists(DATABASE_PATH):
            os.makedirs(DATABASE_PATH, exist_ok=True)


    def create_all_tables(self):
        Base.metadata.create_all(Engine)

    def get_session(self):
        return self.session()

db_manager = DatabaseManager()

def database_file_exists():
    return os.path.exists(DATABASE_PATH)