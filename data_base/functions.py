from .models import User
from .misc import session


class Datafunc():
    @staticmethod
    def get_user(id):
        user = session.query(User).filter_by(id=id).first()
        return user
    

    @staticmethod
    def add(obj):
        if obj != None:
            session.add(obj)
            session.commit()


    @staticmethod
    def commit():
        session.commit()