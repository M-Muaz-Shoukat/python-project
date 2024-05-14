from db.db_manager import DBManager

class Base:
    @staticmethod
    def load(**kwargs):
        return DBManager.read(**kwargs)

    @staticmethod
    def save(**kwargs):
        DBManager.save(**kwargs)
    
    @staticmethod
    def update(**kwargs):
        DBManager.update(**kwargs)
    
    @staticmethod
    def delete(**kwargs):
        DBManager.delete(**kwargs)