"""Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. 
A palindrome is a word that reads the same backwards as forwards """

t=input('enter text')
t2=t[::-1]
if t==t2:
    print ('Paledrom')
else:
    print ('not palendrom')
