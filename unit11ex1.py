"""
Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a 
dictionary whose keys are the product names and whose values are the prices. When the user is done entering
products and prices,allow them to repeatedly enter a product name and print the corresponding price or a 
message if the product is not in the dictionary. """

D = {}
while True:
    prod = input('Enter product : ' )
    if prod == '-1':
        break
    s = eval(input('Enter price : '))
    D [prod] = s

q = input('Check product : ')
if q not in D:
    print('No such product')
else :
    print(D[q])