""" Write a program that asks the user to enter a word. Rearrange all the letters of the word in alphabetical 
order and print out the resulting word. For example, abracadabra should become aaaaabbcdrr. """


t = input('Enter the word : ')
y = sorted(t)
print(y)
s = ''.join(y)
print(s)



