""" Write a program that asks the user for a number and prints
    out the factorial of that number """

number = int(input(' enter a number '))
summ = 1

for i in range(1,number+1):
    summ = summ * i
    print(summ)
    
    
print (summ)
