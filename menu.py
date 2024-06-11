
class Menu():
    def __init__(self,menu_id,name,price,quantity):
        self.menu_id = menu_id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return str(self.menu_id)+","+self.name+","+str(self.price)+","+str(self.quantity)+"\n"
