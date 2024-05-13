from db.db_manager import DBManager

class Base:
    @staticmethod
    def load(file_path):
        return DBManager.read(file_path)

    @staticmethod
    def save(file_path, data):
        DBManager.save(file_path, data)