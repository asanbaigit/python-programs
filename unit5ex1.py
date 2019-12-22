# Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
count=0
for i in range(2,101):
    y=str(i*i)
    if str(y[-1]) == '1':
        count=count+1
        print(count,'----',i,'-----',y)
        