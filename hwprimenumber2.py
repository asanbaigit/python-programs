# another version of finding prime numbers between 1 and 1000
c=0
for i in range (2,1001):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag = 1
    if flag == 0:
            print(i,end=' ')
            c=c+1
print('\n',c)

