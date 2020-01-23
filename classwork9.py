s = eval(input('Enter the size : '))
L = [[0]*s for i in range(s)]
for i in range(s):
    L[i][i]=1
    L[i][-i-1] = 1 # this is for reverse i
for row in L:
    for col in row:
        print(col,end='  ')
    print()
    