"""
 (a) Write a program that asks the user to enter a sentence and then randomly rearranges the words of the sentence.
  Don’t worry about getting punctuation or capitalization correct. (b) Do the above problem, but now make sure that the 
  sentence starts with a capital, that the original ﬁrst word is not capitalized if it comes in the middle of the 
  sentence, and that the period is in the right place. """
from random import shuffle
#a
t = input('enter the text')
y = t.split()
shuffle(y)
print(y)
#b
z = input('enter the text ')
z = z.lower()
x = z.split()
shuffle(x)
k = x[0].capitalize()
del x[0]
x.insert(0,k)
print(x)