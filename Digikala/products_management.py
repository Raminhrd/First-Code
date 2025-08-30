from user_management import user_management

class products_management :
    def __init__(self):
        self.products_list = []


    def add_product(self , name , price , stock , username) :
        new_product = Product(name , price , stock , username )
        if user_management.add_user(type) == 1 : 
            self.products_list.append(new_product)

    def get_products_list(self) :
        return self.products_list
    
    def read_list_customer(self) :
        if user_management.add_user(type) == 2 :
            print('products list is : ' , self.products_list)


class Product : 
    number_of_products = 0

    def __init__(self , name , price , stock, seller_username):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller_username = seller_username
        self.id = Product.number_of_products
        Product.number_of_products += 1