from db.DBManager import db_manager

class VariantOption:
    def __init__(self,name):
        self.name = name

    def get_variant(self,id):
        return {
            "id": id,
            "name": self.name,
        }
    
    @staticmethod
    def get_variants():
        return db_manager.read('./db/data/variants.json')
        
    @staticmethod
    def write_variants(data):
        db_manager.save('./db/data/variants.json',data)
    
