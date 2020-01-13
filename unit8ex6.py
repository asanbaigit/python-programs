"""Write a simple lottery drawing program. The lottery drawing should consist of six different numbers between 1 and 48 """
from random import sample
l = [i for i in range (1,49)]
t = sample(l,6)
print (t)
