class Item:
    pay_rate = 0.8 # the pay after 20% discount
    all = []


    def __init__(self,name:str,price:float,quantity=0):
        #Run vlaidations to the recieved arguments
        assert price>=0,f"Price {price} is not greater thatn or equal to 0"
        assert quantity >=0,f"Qauantity {quantity} is not greater thatn or equal to 0"
        #Assign to self object
        self.name = name,
        self.price = price
        self.quantity = quantity

        #Actio to execute
        Item.all.append(self)
        
        
    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_discount(self):
        self.price *=self.pay_rate    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
   

class Phone(Item):
    all=[]
    def __init__(self,name:str,price:float,quantity=0,broken_phones = 0):
        #Run vlaidations to the recieved arguments
        assert price>=0,f"Price {price} is not greater thatn or equal to 0"
        assert quantity >=0,f"Qauantity {quantity} is not greater thatn or equal to 0"
        assert broken_phones >=0
        #Assign to self object
        self.name = name,
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        #Actio to execute
        Phone.all.append(self)
phone1= Item("jscPhonev10",500,5)
print(phone1.calculate_total_price())
Phone2 = Item("jscPhonev20",500,5)
Phone2.broken_phones = 1    



















