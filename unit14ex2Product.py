"""
Write a class called Product. The class should have ﬁelds called name, amount, and price, holding the 
product’s name, the number of items of that product in stock, and the regular price of the product. There 
should be a method get_price that receives the number of items to be bought and returns a the cost of buying
that many items, where the regular price is charged for orders of less than 10 items, a 10% discount is 
applied for orders of between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. 
There should also be a method called make_purchase that receives the number of items to be bought and 
decreases amount by that much. """

class Product:
    def __init__(self, n, a, p):
        self.name = n
        self.amount = a
        self.price = p
    
    def __str__(self):
        return self.name + ' ' + str(self.amount) + ' ' + str(self.price)

    def get_price(self, n):
        if n < 10:
            return self.price * n
        elif n >= 10 and n <= 99:
            return self.price * n * 0.9
        else:
            return self.price * n * 0.8
    
    def make_purchase(self, n):
        if n > self.amount:
            print('n must be smaller than amount!!!')
        self.amount = self.amount - n