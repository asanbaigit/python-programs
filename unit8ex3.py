""""
(a) Ask the user to enter a sentence and print out the third word of the sentence. 
(b) Ask the user to enter a sentence and print out every third word of the sentence. """
#a
t = input('enter the text')
t = t.split()
print (t[2])
#b
s = input('enter the text')
s = s.split()
for i in range (len(s)):
    if i % 3 == 0:
        print(s[i])
