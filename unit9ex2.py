"""
 (a) Write a program that uses a while loop (not a for loop)to read through a string and print 
 the characters of the string one-by-one on separate lines. (b) Modify the program above to print out every 
 second character of the string. """

#a 
string = 'python'
i = 0
while i < len(string):
    print(string[i])
    i += 1
#b
string = 'python'
i = 0
while i < len(string):
    print(string[i])
    i = i + 2