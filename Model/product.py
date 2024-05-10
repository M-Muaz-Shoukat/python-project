from db.DBManager import db_manager

class Product:
    def __init__(self,id,name,description,status,img_path,variations):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.img_path = img_path
        self.variations = variations

    def get_product(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "img_path": self.img_path,
            "variations": self.variations
        }
    @staticmethod
    def get_products():
        return db_manager.read('./db/data/products.json')

    @staticmethod
    def write_products(data):
        db_manager.save('./db/data/products.json',data)
    

