"""
Write a program that allows the user to enter any number of test scores. The user indicates they are done by 
entering in a negative number. Print how many of the scores are A’s (90 or above). Also print out the average.
"""
score = 0 
count = 0
total = 0
highscore = 0
while score > -1 :
    score = eval(input('enter your scores '))
    if score < 0 :
        break
    elif score >=90:
        highscore = highscore + 1
    count = count + 1
    total = total + score
print ('---------')
print('You have ',count,' scores' )
print ('You have ',highscore,' A scores',)
print('Your average score is :',(total/count))



    
