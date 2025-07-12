from model.database_manager import db_manager
from .data_models import User
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

class UserModel:
    def __init__(self):
        db_manager.create_all_tables()

    def add_user(self, name, lastname):
        session = db_manager.session()
        try:
            new_user = User(name=name, last_name=lastname)
            session.add(new_user)
            session.commit()
            return new_user
        except IntegrityError:
            session.rollback()
            return None
        finally:
            session.close()

    def get_all_users(self):
        session = db_manager.session()
        try:
            users = session.query(User).all()
            return [u.to_dict() for u in users]
        except Exception as e:
            return []
        finally:
            session.close()

    def get_user_by_id(self, user_id):
        session = db_manager.session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            return user.to_dict() if user else None
        except Exception as e:
            return None
        finally:
            session.close()

    def update_user(self, user_id, new_name=None, new_last_name=None):
        session = db_manager.session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                if new_name:
                    user.name = new_name
                if new_last_name:
                    user.last_name = new_last_name
                session.commit()
                return user.to_dict()
            else:
                return None
        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()

    def delete_user(self, user_id):
        session = db_manager.session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()

user_model = UserModel()