""" Recall that, given a string s, s.index('x') returns the index of the ﬁrst x in s and an error if there is 
no x. (a) Write a program that asks the user for a string and a letter. Using a while loop, the program should 
print the index of the ﬁrst occurrence of that letter and a message if the string does not contain the letter. 
(b) Write the above program using a for/break loop instead of a while loop."""
#a
""" This is working wrong when letter not found in str
i = 0
s = input('Enter a string : ')
l = input('Enter a letter : ')

while len(s) > i:
    if l not in s:
        print('string does not contain the letter')
        break
    else:
        i = i + 1
        k=s.index(l)
print(k, 'is the index of the ﬁrst occurrence of the letter',l) """

#b
"""
s = input('Enter a string : ')
l = input('Enter a letter : ')
for i in range (len(s)) :
    if l not in s:
        print('string does not contain the letter')
        break
    else:
        k=s.index(l)
print(k, 'is the index of the ﬁrst occurrence of the letter',l) """

#solution by teacher in class :
s = input('Enter a string : ')
k = 0
flag = False
while k < len(s):
    if s[k] == 'x':
        flag = True
        break
    k = k + 1
if flag:
    print(k)
else:
    print('not found')
