class user_management :
    def __init__(self) :
            self.user_list = []
            self.seller_list = []
            self.customer_list = []

    def add_user(self) :
          username = input('enter your username : ' )
          type = int(input('enter youer type ( if you are seller enter 1 if you are customer enter 2 ) : ' ))
          if type == 1 or type == 2 :
            self.user_list.append({'name' : username , 'type' : type})

          if type == 1 : 
              self.seller_list.append(username)

          if type == 2 :
                self.customer_list.append(username)

          if type > 2 :
                print('Invalid Type')
            
            
    def Seller(self) :
          print('seller is : ' , self.seller_list)


    def Customer(self) :
          print('cutomer is : ' , self.customer_list)


user = user_management()
user.add_user()
user.Customer()
user.Seller()