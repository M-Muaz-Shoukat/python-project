from db.DBManager import db_manager
from Model.product import Product
from Model.variant import Variant
from Model.variant_option import VariantOption
from tabulate import tabulate
import sys

def clear_console():
    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()


class Inventory_Manager:
    def __init__(self):
        self.products = Product.get_products()
        self.variants = VariantOption.get_variants()


    def create_variant(self,name):
        variant = VariantOption(name)
        data = variant.get_variant(len(self.variants))
        self.variants.append(data)
        VariantOption.write_variants(self.variants)
        print('\n\n Vaiant Created Successfully \n\n')

    def delete_variant(self,id):
        self.variants = [variant for variant in self.variants if variant['id']!=id]
        VariantOption.write_variants(self.variants)
        print('\n\n Variant Deleted Successfully \n\n')

    def update_variant(self, id, name=None):
        for variant in self.variants:
            if variant['id'] == id:
                if name != '':
                    variant['name'] = name
                VariantOption.write_variants(self.variants)
                print('\n\n Variant Updated Successfully \n\n')
                return
        print("\n\n Variant not found \n\n")

    def print_variants(self):
        data = []
        for x in self.variants:
            data.append([x['id'], x['name']])
        headers = ["ID", "Name"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def compare_objects(arr1, arr2):
        if len(arr1) != len(arr2):
            return 0
        arr1.sort(key=lambda x: x['name'])
        arr2.sort(key=lambda x: x['name'])
        for obj1, obj2 in zip(arr1, arr2):
            if obj1['name'] != obj2['name'] or obj1['value'] != obj2['value']:
                return 0 
        return 1   
    
    def create_product(self,name,description,status,img_path):
        variations = []
        flag = True
        print('Add Variations:')
        while flag:
            print('Choose variant Index:')
            for index,var in enumerate(self.variants):
                print(f'{index} -- name: {var['name']}')
            variantIndexes = input('choose all variants seperated by space like this(1 2 3 4): ')
            variantIndexes = variantIndexes.strip().split(' ')
            variantIndexes = [self.variants[int(x)] for x in variantIndexes]
            for variantOption in variantIndexes:
                value = input(f'Enter value for variant {variantOption['name']}: ')
                variantOption['value'] = value
            quantity = int(input('Enter Quantity: '))
            price = float(input('Enter Price: '))
            variant = Variant(len(variations),quantity,price,variantIndexes)
            curvariant = variant.get_product_variant()
            existingFlag = 0
            for var in variations:
                if self.compare_objects(curvariant['variants'], var['variants']):
                    existingFlag = 1 

            if existingFlag == 1:
                print("Variant already exists")
            else:
                variations.append(variant.get_product_variant())  
                
            if(int(input('0 --> Want to add more\n1 --> Done with variations\nchoose: '))):
                break
        product = Product(len(self.products),name,description,status,img_path,variations)
        self.products.append(product.get_product())
        Product.write_products(self.products)
        print('\n\n product Created Successfully \n\n')

    def delete_product(self,id):
        self.products = [product for product in self.products if product['id']!=id]
        Product.write_products(self.products)
        print('\n\n product Deleted Successfully \n\n')

    def update_product(self, id):
        for product in self.products:
            if product['id'] == id:
                editOption = input('1 --> Edit Product details\n2 --> Edit Product variations\nChoose option: ')
                match editOption:
                    case '1':
                        name = input('New Product Name (leave empty to keep unchanged): ')
                        description = input('New Product Description (leave empty to keep unchanged): ')
                        print('Status:')
                        for index, status in enumerate(statusArray):
                            print(f'{index} for {status}')
                        status_input = input('Choose new status Index (leave empty to keep unchanged): ')
                        status_index = int(status_input) if status_input else None
                        status = statusArray[status_index] if status_index is not None else None
                        img_path = input('New Image Path (leave empty to keep unchanged): ')
                        if name != '':
                            product['name'] = name
                        if description != '':
                            product['description'] = description
                        if status is not None:
                            product['status'] = status
                        if img_path != '':
                            product['img_path'] = img_path
                    case '2':
                        while True:
                                for index,variant in enumerate(product['variations']):
                                    print(f'\t{index} --> Quantity: {variant['quantity']} -- Price: {variant['price']}')
                                    for variantOpt in variant['variants']:
                                        print(f'\t\t\tVariant : {variantOpt['name']} : {variantOpt['value']}')
                                
                                editVariation = int(input('Choose variant(id): '))
                                print('Choose variant Index:')
                                for index,var in enumerate(self.variants):
                                    print(f'{index} -- name: {var['name']}')
                                variantIndexes = input('choose all variants seperated by space like this(1 2 3 4) (leave empty to keep unchanged): ')
                                if(variantIndexes != ''):
                                    variantIndexes = variantIndexes.strip().split(' ')
                                    variantIndexes = [self.variants[int(x)] for x in variantIndexes]
                                    for variantOption in variantIndexes:
                                        value = input(f'Enter value for variant {variantOption['name']}: ')
                                        variantOption['value'] = value
                                quantity = input('Quantity (leave empty to keep unchanged): ')
                                price = input('Price (leave empty to keep unchanged): ')
                                # print("variantIndexes",variantIndexes)
                                if quantity != '':
                                    product['variations'][editVariation]['quantity'] = int(quantity)
                                if price != '':
                                    product['variations'][editVariation]['price'] = int(price)
                                if variantIndexes != '':
                                    product['variations'][editVariation]['variants'] = variantIndexes
                                next_step = input('1 --> Want to change more\n2 --> Done with variations\nChoose: ')
                                if(next_step != '1'):
                                    break
                    case _:
                        pass
                Product.write_products(self.products)
                print('\n\n Product Updated Successfully \n\n')
                return
        print("\n\n Product not found \n\n")


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



    # def print_products(self):
    #     for product in self.products:
    #         print(f'id: {product['id']} -- name: {product['name']} -- status: {product['status']}')
    #         print(f'description: {product['description']}')
    #         print('variations: ')
    #         for variant in product['variations']:
    #             print(f'\tid: {variant['id']} -- quantity: {variant['quantity']} -- price: {variant['price']}')
    #             for var in variant['variants']:
    #                 print(f'\t\t name: {var['name']} -- value: {var['value']}')
    #             print()

ivm = Inventory_Manager()
statusArray = ['active','inactive']
while True:
    print('0 --> Create Product\n1 --> Print Products\n2 --> Delete Product\n3 --> Create Variant\n4 --> Print Variants\n5 --> Delete Variant\n6 --> Update Product\n7 --> Update Variant\nAnything else to exit\n')
    option = input("Choose option: ")
    match option:
        case '0':
            clear_console()
            name = input('Product Name: ')
            print('Status:')
            for index,status in enumerate(statusArray):
                print(f'{index} for {status}')
            status = int(input('Choose status Index: '))
            status = statusArray[status]
            description = input('Product Description: ')

            ivm.create_product(name,description,status,'')
        case '1':
            clear_console()
            ivm.print_products()
        case '2':
            clear_console()
            ivm.print_products()
            id = int(input('Product to delete(id):'))
            ivm.delete_product(id)
        case '3':
            clear_console()
            name = input("Variant Name: ")
            ivm.create_variant(name)
        case '4':
            clear_console()
            ivm.print_variants()
        case '5':
            clear_console()
            ivm.print_variants()
            id = int(input('Variant to delete(id):'))
            ivm.delete_variant(id)
        case '6':
            clear_console()
            ivm.print_products()
            id = int(input('Product to update(id): '))
            ivm.update_product(id)
        case '7':
            clear_console()
            ivm.print_variants()
            id = int(input('Variant to update(id): '))
            name = input('New Variant Name (leave empty to keep unchanged): ')
            ivm.update_variant(id, name)
        case _:
            break













