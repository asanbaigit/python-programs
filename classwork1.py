# finding MAX and MIN

maks  = eval(input('Enter a positive number: '))
mini = maks 
maks2=0
for i in range(2): 
    n = eval(input('Enter a positive number: '))
    if n>maks:
        maks=n
        if n>maks2:
            maks2=n
    if n<mini:
        mini=n

print('Max:',maks, 'Min:',mini)
print(maks2)
