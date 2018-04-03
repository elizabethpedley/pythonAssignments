class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    
    def sell(self):
        self.status = 'sold'
        return self
    
    def add_tax(self):
        return self.price * 1.12

    def returns(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in box':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price *= 0.80
        else:
            print "That is not a valid reason for a return"
        return self
    def display_all(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for attribute in attributes:
            print attribute+ ': ' + str(getattr(self, attribute))
