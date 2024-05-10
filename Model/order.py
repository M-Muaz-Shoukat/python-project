from db.DBManager import db_manager

class OrderItem:
    def __init__(self, id,product_id, quantity,price):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def get_order_item(self):
        return {
            "id": self.id,
            "product_Id": self.product_id,
            "quantity": self.quantity,
            "price": self.price
        }
        

class Order:
    def __init__(self, order_id, customer_info,order_items):
        self.order_id = order_id
        self.customer_info = customer_info
        self.order_items = order_items

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.order_items)
        return total


    def get_order(self):
        return {
            "id": self.order_id,
            "customer_info": self.customer_info,
            "order_items": self.order_items,
            "total_bill": self.calculate_total()
        }    

    @staticmethod
    def get_orders():
        return db_manager.read('./db/data/orders.json')

    @staticmethod
    def write_orders(data):
        db_manager.save('./db/data/orders.json',data)


