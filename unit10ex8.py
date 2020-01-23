"""
Write a program to ﬁnd all numbers between 1 and 1000 that are divisible by 7 and end in a 6. """

for i in range (1,1001):
    if i % 7 == 0 and str(i)[-1] == '6': #  i % 10 == 6    ..... the same thing
        print(i)
