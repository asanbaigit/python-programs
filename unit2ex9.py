# The Fibonacci numbers are the sequence below,
# where the ﬁrst two numbers are 1,
# and each number thereafter is the sum of the two preceding numbers.
# Write a program that asks the user how many Fibonacci numbers to print
# and then prints that many.
# 1,1,2,3,5,8,13,21,34,55,89...

a=1
b=1
c=0

answer = int(input('how many Fibonacci numbers do you want to print? '))

for i in range (answer):
    c=a+b
    a=b
    b=c
    print (i+1,'---',c)
             
