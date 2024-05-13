from db.db_manager import DBManager
from model.base import Base

class Variant(Base):
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    # @staticmethod
    # def get_variants():
    #     return DBManager.read('./db/data/variants.json')
        
    # @staticmethod
    # def write_variants(data):
    #     DBManager.save('./db/data/variants.json',data)
    
