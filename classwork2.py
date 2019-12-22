# 1-2+3-4+5-6 .... + 1999 - 2000 == ?
summ=0
for i in range (1,2001):
    if i%2 == 1:
        print ('+',i,sep='',end='')
        summ=summ+i
    else:
        print ('-',i,sep='',end='')
        summ=summ-i
print('=',summ,sep='')