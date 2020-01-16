"""i = 0
while i < 101:
    print (i,end=' ')
    i = i+1 """
n = 0
s = 0
c = 0
while (True):
    s = s + n
    n = eval(input('enter num '))
    if n == -1:
        break
    else:
        c = c + 1
    
print ('total =', s)
print('average = ',s/c)
