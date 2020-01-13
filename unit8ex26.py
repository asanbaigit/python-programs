"""  We usually refer to the entries of a two-dimensional list by their row and column, like below on the left.
 Another way is shown below on the right.
(0,0) (0,1) (0,2) 0 1 2 
(1,0) (1,1) (1,2) 3 4 5 
(2,0) (2,1) (2,2) 6 7 8
(a) Write some code that translates from the left representation to the right one. 
The // and % operators will be useful. Be sure your code works for arrays of any size. 
(b) Write some code that translates from the right representation to the left one. """

row_size = eval(input('enter row size : '))
col_size = eval(input('enter column size : '))

# a)
for i in range(row_size):
    for j in range(col_size):
        print('(',i,',',j,')', sep='', end='')
    print()

# b) using nested for range
c = 0
for i in range(row_size):
    for j in range(col_size):
        print(c, end=' ')
        c = c + 1
    print()

# b) using one for range

for k in range(row_size*col_size):
    print(k, end=' ')
    if (k+1)%col_size == 0:
        print()