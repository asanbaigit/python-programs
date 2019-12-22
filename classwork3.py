# find perfect numbers between 1 and 10 000
# 6 is perfect number because sum of its divisors is equal to 6
for i in range(1,100):
    s=0
    for j in range(1,i):
        if i % j == 0:
            #print(i)
            s=s+j
    if s == i:
        print(i,end='->')
        for k in range (1,i):
            if i%k == 0:
                print(k,end=' ')
        print()