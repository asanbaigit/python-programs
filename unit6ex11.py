"""Write a program that asks the user to enter a word that contains the letter a. The program should then print
the following two lines: On the ﬁrst line should be the part of the string up to and including the the ﬁrst a,
and on the second line should be the rest of the string. Sample output is shown below:
Enter a word: buffalo buffa lo """
t=input('Enter a word that contains the letter a ')
if 'a' not in t:
    print('error!!! Enter a word that contains the letter a')
else:
    print(t[:(t.index('a')+1)],'\n',t[(t.index('a')+1):])
