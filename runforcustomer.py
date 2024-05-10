from db.DBManager import db_manager
from Model.product import Product
from Model.variant import Variant
from Model.variant_option import VariantOption
from Model.order import Order
from Model.order import OrderItem
from tabulate import tabulate
import json
import sys

def clear_console():
    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()

class order_item:
    def __init__(self,productId,quantity):
        self.productId: productId
        self.quantity: quantity

    def get_orderitem(self,id):
        return {
            "productId": self.productId,
            "quantity": self.quantity
        }


class order:
    def __init__(self,items):
        self.items = items

    def get_order(self,id):
        return {
            "id": id,
            "items": self.productId,
            "quantity": self.quantity
        }
    
class Inventory_Manager:
    def __init__(self):
        self.products = Product.get_products()
        self.variants = VariantOption.get_variants()
        self.orders = Order.get_orders()

    def print_variants(self):
        data = []
        for x in self.variants:
            data.append([x['id'], x['name']])
        headers = ["ID", "Name"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def print_products(self):
        for product in self.products:
            print(f'id: {product["id"]} -- name: {product["name"]} -- status: {product["status"]}')
            print(f'description: {product["description"]}')
            print('variations: ')
            variations_data = []
            for variant in product['variations']:
                variations_data.append([
                    variant['id'],
                    variant['quantity'],
                    variant['price']
                ])
            print(tabulate(variations_data, headers=["ID", "Quantity", "Price"], tablefmt="grid"))
            for variant in product['variations']:
                print(f'\nVariant {variant["id"]} details:')
                variant_data = []
                for var in variant['variants']:
                    variant_data.append([
                        var['name'],
                        var['value']
                    ])
                print(tabulate(variant_data, headers=["Name", "Value"], tablefmt="grid"))

    def create_order(self):
        order_items = []
        customerInfo = {
            "name": '',
            "email": ''
        }
        customerInfo['name'] = input("Enter customer name: ")
        customerInfo['email'] = input("Enter customer email: ")
        self.print_products()
        while True:
            product_id = int(input("Enter product ID (or type -1 to finish adding items): "))
            if product_id == -1:
                break
            product_found = [p for p in self.products if product_id == p['id']][0]
            if product_found is None:
                print(f"Error: Product with ID '{product_id}' not found")
                continue
            variations_data = []
            for variant in product_found['variations']:
                variations_data.append([
                    variant['id'],
                    variant['quantity'],
                    variant['price']
                ])
            print(tabulate(variations_data, headers=["ID", "Quantity", "Price"], tablefmt="grid"))
            variant_id = int(input("Enter variant ID: "))
            variant_found = [v for v in product_found['variations'] if variant_id == v['id']][0]
            if variant_found is None:
                print(f"Error: Variant with ID '{variant_id}' not found")
                continue
            quantity = int(input("Enter quantity: "))     
            if (variant_found['quantity'] < quantity):
                print(f"Error: Insufficient stock for product '{product_found['name']}'")
                continue
            order_item = OrderItem(len(order_items),product_id,quantity,variant_found['price'])
            order_items.append(order_item.get_order_item())
        self.place_order(order_items,customerInfo)
        # return order_items

    def place_order(self, order_items,customerInfo):
        order = Order(len(self.orders),customerInfo,order_items)
        data = order.get_order()
        self.orders.append(data)
        Order.write_orders(self.orders)
        print(f"\n\nOrder placed successfully\n\n")      

    def print_orders(self):
        if self.orders:
            print("All Orders:")
            for order in self.orders:
                print('order',order)
                order_id = order['id']
                customer_name = order['customer_info']['name']
                total_bill = order['total_bill']
                
                # Prepare data for order items
                order_items_data = []
                for item in order['order_items']:
                    product_id = item['product_Id']
                    quantity = item['quantity']
                    price = item['price']
                    product = next((p for p in self.products if p['id'] == product_id), None)
                    if product:
                        order_items_data.append([product['name'], quantity, price])
                
                # Print order details and items table
                print(f"Order ID: {order_id}, Customer: {customer_name}, Total Bill: {total_bill}")
                print(tabulate(order_items_data, headers=["Product", "Quantity", "Price"], tablefmt="grid"))
                print()
        else:
            print("No orders found.")  
            

    def print_products_by_category(self,catId):
        for product in [product for product in self.products if product["category"]["id"] == catId]:
            print(f'id: {product['id']} -- name: {product['name']} -- status: {product['status']}')
            print(f'description: {product['description']}')
            print(f'category: {product["category"]["name"]}')
            print('variations: ')
            for variant in product['variations']:
                print(f'\tid: {variant['id']} -- quantity: {variant['quantity']} -- price: {variant['price']}')
                for var in variant['variants']:
                    print(f'\t\t name: {var['name']} -- value: {var['value']}')
                print()

ivm = Inventory_Manager()
statusArray = ['active','inactive']
while True:
    print('0 --> Print Products\n1 --> Print Variants\n2 --> Make Order\n3 --> View Orders\nAnything else to exit\n')
    option = input("Choose option: ")
    match option:
        case '0':
            ivm.print_products()
        case '1':
            ivm.print_variants()
        case '2':
            ivm.create_order()
        case '3':
            ivm.print_orders()
        case _:
            break













