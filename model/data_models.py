from sqlalchemy import Column, Integer, String, Float
from model.database_manager import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name}, last_name={self.last_name})>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
        }