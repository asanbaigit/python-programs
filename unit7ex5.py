"""
Ask the user to enter a list of strings. Create a new list that consists of those strings 
with their ﬁrst characters removed. """

L = ['Hello','Python','Java']
M = []

for i in range (len(L)) :
    a = L[i][1:]
    M.append(a)
print(M)