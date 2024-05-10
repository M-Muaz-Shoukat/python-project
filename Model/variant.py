
class Variant:
    def __init__(self,id,quantity,price,variants):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.variants = variants

    def get_product_variant(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "price": self.price,
            "variants": self.variants
        }
    

        