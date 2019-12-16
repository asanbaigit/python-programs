"""A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, 
the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a program that asks 
the user how many items they are buying and prints the total cost."""

item=int(input('Enter the number of items you are buying '))
if item < 10:
    print(item,' items * 12 $ Total cost is', item*12,' $')
elif 10<=item<=99:
    print (item,' items * 10 $ Total cost is', item*10,' $')
else:
    print (item,' items * 7 $ Total cost is', item*7,' $')
