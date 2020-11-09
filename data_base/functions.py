from .models import User, PicturesTruth, PicturesAction
from .misc import session


class Datafunc():
    @staticmethod
    def get_user(id):
        user = session.query(User).filter_by(id=id).first()
        return user
    

    @staticmethod
    def add(obj):
        if obj != None:
            try:
                session.add(obj)
                session.commit()
            except:
                session.rollback()


    @staticmethod
    def commit():
        try:
            session.commit()
        except:
            session.rollback()



    @staticmethod
    def get_acts():
        return session.query(PicturesAction).all()

    @staticmethod
    def get_truth():
        return session.query(PicturesTruth).all()


    @staticmethod
    def get_pic_truth(id):
        return session.query(PicturesTruth).filter_by(id=id).first()
    @staticmethod
    def get_pic_act(id):
        return session.query(PicturesAction).filter_by(id=id).first()
    
    @staticmethod
    def search_act(filename):
        return session.query(PicturesAction).filter_by(filename=filename).first()

    @staticmethod
    def search_truth(filename):
        return session.query(PicturesTruth).filter_by(filename=filename).first()
        