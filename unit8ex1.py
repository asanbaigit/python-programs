"""Write a program that asks the user to enter some text and then counts how many articles are in the text.
 Articles are the words 'a', 'an', and 'the'. """


t = input('enter the text ')
q = t.split(' ')
print(q)

s = q.count('a')
y = q.count('an')
z = q.count ('the')

print(s,y,z)