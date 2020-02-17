from unit14ex2Product import Product

p = Product('Apple', 100, 10.0)
print(p)
#print(p.get_price(100))
n = eval(input('kancha shtuk alasin? '))
print(p.get_price(n))
p.make_purchase(n)
print(p)