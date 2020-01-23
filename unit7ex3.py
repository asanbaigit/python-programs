"""
Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17 (b) Add 4, 5, and 6 to the end of the list 
(c) Remove the ﬁrst entry from the list (d) Sort the list (e) Double the list (f) Insert 25 at index 3
The ﬁnal list should equal [4,5,6,25,10,17,4,5,6,10,17] """

L = [8,9,10]
L[1] = 17 #a
print(L)
s = [4,5,6] #b
p = L + s
print(p)
del p[0] #c
print(p)
p.sort() # d
print(p)
p = p*2 # e
print(p)
p.insert(3,25) # f
print(p)