#Author Isaac Corcia

class: shoppingCart

 def __init__(self, cartDetails: list):
        
        self.user = cartDetails[0]
        self.isbn = cartDetails[1]
        self.title = cartDetails[2]
        self.price = cartDetails[3]
        self.quantity = cartDetails[4]