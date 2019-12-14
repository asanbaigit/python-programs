# diamond

height = int(input('enter height '))


for i in range(1,height+1,2):
    print(' '*((height-i)//2),'*'*i, sep='')


for k in range (i - 2, 0,-2):
    print(' '*((i-k)//2),'*'*k, sep='')

