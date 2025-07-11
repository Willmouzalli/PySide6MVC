from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL, DATABASE_PATH

Base = declarative_base()
Engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=Engine)

import os
def database_file_exists():
    return os.path.exists(DATABASE_PATH)