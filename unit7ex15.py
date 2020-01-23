""" (a) Write a program that asks the user for a message and encrypts the message using the one-time pad. First
convert the string to lowercase. Any spaces and punctuation in the string should be left unchanged. For example,
 Secret!!! becomes thebmv!!! using the shifts above. 
 (b) Write a program to decrypt a string encrypted as above. """
from random import randint
from string import ascii_lowercase
from string import punctuation
letters = ascii_lowercase
encr = ''
L = []
s = input('Enter string : ')
for i in range (len(s)):
    if s[i] not in punctuation:
        n = randint(1,26)
        L.append(n)
        shift_size = (n + letters.index(s[i]))%26
        encr = encr + letters[shift_size]
    else:
        encr = encr + s[i]
print(encr) 
print(L)
decr = ''
for e in encr :
    if e not in punctuation:
        n = L[0]
        del L[0]
        shift_size = (letters.index(e) - n + 26)%26
        decr = decr + letters[shift_size]
    else :
        decr = decr + e
print(decr)
