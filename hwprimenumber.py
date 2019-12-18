# Find prime numbers between 1 and  1000
howmany=0
for num in range(1,1001):
    c=0
    for j in range(1,num+1):
        if num % j == 0:
            c=c+1
    if c == 2:
        howmany=howmany+1
        print (num, 'is a prime number')
print('The are ',howmany,' prime numbers between 1 and 1001' )
    
        
            