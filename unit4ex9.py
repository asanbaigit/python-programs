""" Write a program that asks the user to enter a number and prints out all the divisors of that number.
 [Hint: the % operator is used to tell if a number is divisible by something """

ans=int(input('Enter a number '))
c=0
for i in range (1,ans+1):
     if ans%i==0:
         c=c+1
         print(i,end=" ")
print()
print(ans,'is divisible by',c,'numbers')
