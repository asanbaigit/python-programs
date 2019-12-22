"""Write a program that asks the user to enter a string. The program should then print the following:
(a) The total number of characters in the string (b) The string repeated 10 times 
(c) The ﬁrst character of the string (remember that string indices start at 0) 
(d) The ﬁrst three characters of the string (e) The last three characters of the string (f) The string backwards 
(g) The seventh character of the string if the string is long enough and a message otherwise 
(h) The string with its ﬁrst and last characters removed (i) The string in all caps 
(j) The string with every a replaced with an e (k) The string with every letter replaced by a space """

X=input('Enter a string ')
print(len(X))
print(X*10)
print(X[0])
print(X[ :3])
print(X[-3: ])
print(X[::-1])
print(X[6])
print(X[1:(len(X)-1)])
print(X.upper())
print(X.replace('a','e'))
print(X.replace('',''))
if X.isalpha():
    print('is alpha')