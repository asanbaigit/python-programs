"""Pascal’s triangle is shown below. On the outside are 1’s and each other number is the sum of the two 
numbers directly above it. Write a program to generate Pascal’s triangle. 
Allow the user to specify the number of rows. Be sure that it is nicely formatted """
"""
row = eval(input('enter row : '))
l = []
for i in range (row):
    l.append([])
    l[i].append(1)
    for j in range (1,i):
        l[i].append(l[i-1][j-1] + l[i-1][j])
    if (row != 0):
        l[i].append(1)
for i in range (row):
    print('   '*(row-i),end=' ', sep=' ')
    for j in range(0,i+1):
        print('{0:6}'.format(l[i][j]),end=' ', sep=' ')
    print()"""
    
    # solution in class
t_size = eval(input('enter size : '))
L = []
for i in range (1,t_size+1):
    L = L + [[1]*i]
for  i in range (2,t_size):
    for j in range (1,len(L[i])-1):
        L[i][j] = L[i-1][j-1]+L[i-1][j]
print (L)
for l in L :
    sp = t_size - len(l)
    print(' '*sp*2,end='')
    for k in l :
        print('{:^4d}'.format(k), end=' ')
    print()
