"""
Write a program that takes a list of ten prices and ten products, applies an 11% discount to each of the prices 
displays the output like below, right-justiﬁed and nicely formatted.
Apples $ 2.45 
Oranges $ 18.02 
...
Pears $120.03 """
pro = []
pri = []
pri2 = []
for i in range(3):
    product = input('Enter the list of products : ')
    pro.append(product)
    price = eval(input('Enter the price of product : '))
    pri.append(price)
#print (pro,pri)
for j in range(len(pri)):
    disc = float(pri[j]*(0.89))
    pri2.append(disc)
#print(pri2)
for k in range (len(pro)):
    print('{:>6s}'.format(pro[k]), '$','{:.2f}'.format(pri2[k]))    




