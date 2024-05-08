import json

class VariantOption:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def get_variant(self,id):
        return {
            "id": id,
            "name": self.name,
            "value": self.value
        }
    pass

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
        
    pass



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

    def create_product(self):
        pass
    pass

class Inventory_Manager:
    def __init__(self):
        self.get_products()
        self.get_variants()


    def get_variants(self):
        with open("variants.json", 'r') as f:
            self.variants = json.load(f)

    def write_variants(self):
        with open("variants.json", 'w') as f:
            json.dump(self.variants, f, indent=4)

    def create_variant(self,name,value):
        variant = VariantOption(name,value)
        data = variant.get_variant(len(self.variants))
        self.variants.append(data)
        self.write_variants()
        print('\n\n Vaiant Created Successfully \n\n')

    def delete_variant(self,id):
        self.variants = [variant for variant in self.variants if variant['id']!=id]
        self.write_products()
        print('\n\n Variant Deleted Successfully \n\n')

    def update_variant(self, id, name=None, value=None):
        for variant in self.variants:
            if variant['id'] == id:
                if name != '':
                    variant['name'] = name
                if value != '':
                    variant['value'] = value
                self.write_variants()
                print('\n\n Variant Updated Successfully \n\n')
                return
        print("\n\n Variant not found \n\n")



    def print_variants(self):
        for x in self.variants:
            print(f'{x['id']}->{x['name']} -- {x['value']}')
        print()

    def get_products(self):
        with open("products.json", 'r') as f:
            self.products = json.load(f)
    
    def write_products(self):
        with open("products.json", 'w') as f:
            json.dump(self.products,f,indent=4)
    
    def create_product(self,name,description,status,img_path):
        variations = []
        flag = True
        print('Add Variations:')
        while flag:
            quantity = int(input('Enter Quantity: '))
            price = float(input('Enter Price: '))
            print('Choose variant Index:')
            for index,var in enumerate(self.variants):
                print(f'{index} -- name: {var['name']} -- value: {var['value']}')
            variantIndexes = input('choose all variants seperated by space like this(1 2 3 4): ')
            variantIndexes = variantIndexes.strip().split(' ')
            variantIndexes = [self.variants[int(x)] for x in variantIndexes]
            variant = Variant(len(variations),quantity,price,variantIndexes)
            variations.append(variant.get_product_variant())
            if(int(input('0 --> Want to add more\n1 --> Done with variations\nchoose: '))):
                break
        product = Product(len(self.products),name,description,status,img_path,variations)
        self.products.append(product.get_product())
        self.write_products()
        print('\n\n product Created Successfully \n\n')

    def delete_product(self,id):
        self.products = [product for product in self.products if product['id']!=id]
        self.write_products()
        print('\n\n product Deleted Successfully \n\n')

    def update_product(self, id, name=None, description=None, status=None, img_path=None):
        for product in self.products:
            if product['id'] == id:
                if name != '':
                    product['name'] = name
                if description != '':
                    product['description'] = description
                if status is not None:
                    product['status'] = status
                if img_path != '':
                    product['img_path'] = img_path
                self.write_products()
                print('\n\n Product Updated Successfully \n\n')
                return
        print("\n\n Product not found \n\n")



    def print_products(self):
        for product in self.products:
            print(f'id: {product['id']} -- name: {product['name']} -- status: {product['status']}')
            print(f'description: {product['description']}')
            print('variations: ')
            for variant in product['variations']:
                print(f'\tid: {variant['id']} -- quantity: {variant['quantity']} -- price: {variant['price']}')
                for var in variant['variants']:
                    print(f'\t\t name: {var['name']} -- value: {var['value']}')
                print()


    pass


ivm = Inventory_Manager()
statusArray = ['active','inactive']
while True:
    print('0 --> Create Product\n1 --> Print Products\n2 --> Delete Product\n3 --> Create Variant\n4 --> Print Variants\n5 --> Delete Variant\n6 --> Update Product\n7 --> Update Variant\nAnything else to exit\n')
    option = input("Choose option: ")
    match option:
        case '0':
            name = input('Product Name: ')
            print('Status:')
            for index,status in enumerate(statusArray):
                print(f'{index} for {status}')
            status = int(input('Choose status Index: '))
            status = statusArray[status]
            description = input('Product Description: ')

            ivm.create_product(name,description,status,'')
        case '1':
            ivm.print_products()
        case '2':
            id = int(input('Product to delete(id):'))
            ivm.delete_product(id)
        case '3':
            name = input("Variant Name: ")
            value = input ("Variant Value: ")
            ivm.create_variant(name,value)
        case '4':
            ivm.print_variants()
        case '5':
            id = int(input('Variant to delete(id):'))
            ivm.delete_variant(id)
        case '6':
            id = int(input('Product to update(id): '))
            name = input('New Product Name (leave empty to keep unchanged): ')
            description = input('New Product Description (leave empty to keep unchanged): ')
            print('Status:')
            for index, status in enumerate(statusArray):
                print(f'{index} for {status}')
            status_input = input('Choose new status Index (leave empty to keep unchanged): ')
            status_index = int(status_input) if status_input else None
            status = statusArray[status_index] if status_index is not None else None
            img_path = input('New Image Path (leave empty to keep unchanged): ')
            ivm.update_product(id, name, description, status, img_path)
        case '7':
            id = int(input('Variant to update(id): '))
            name = input('New Variant Name (leave empty to keep unchanged): ')
            value = input('New Variant Value (leave empty to keep unchanged): ')
            ivm.update_variant(id, name, value)

        case _:
            break













