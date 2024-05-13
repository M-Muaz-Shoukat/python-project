from db.db_manager import DBManager
from model.base import Base

class Product(Base):
    def __init__(self,id,name,description,status,img_path,variations):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.img_path = img_path
        self.variations = variations

    # @staticmethod
    # def get_products():
    #     return DBManager.read('./db/data/products.json')

    # @staticmethod
    # def write_products(data):
    #     DBManager.save('./db/data/products.json',data)
    

