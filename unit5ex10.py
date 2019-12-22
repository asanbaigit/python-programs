""" Ask the user to enter 10 test scores. Write a program to do the following:(a) Print out the highest and lowest scores. 
(b) Print out the average of the scores.(c) Print out the second largest score. (d) If any of the scores is greater than 
100, then after all the scores have been entered,print a message warning the user that a value over 100 has been entered. 
(e) Drop the two lowest scores and print out the average of the rest of them."""
highest  = eval(input('Enter a score: '))
total=highest
flag=0
if highest > 100:
    flag = 1
for i in range(9):
    score = eval(input('Enter a score: '))
    if highest < score :
        highest = score
    total=total+score
    if score > 100:
        flag = 1
if flag == 0:
        print ('highest = ',highest)
        print('average = ', total/10)
else:
    print('warning')
