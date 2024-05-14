from db.db_manager import DBManager
from model.base import Base

class Variant(Base):
    def __init__(self,id,name):
        self.id = id
        self.name = name
