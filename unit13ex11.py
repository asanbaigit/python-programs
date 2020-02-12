"""
Write a function called matches that takes two strings as arguments and returns how many matches there 
are between the strings. A match is where the two strings have the same character at the same index. 
For instance, 'python' and 'path' match in the ﬁrst, third, and fourth characters, so the function should 
return 3. """

def matches (st1,st2):
    c = 0
    for i in range(min(len(st1),len(st2))):
        if st1[i] == st2[i]:
            c += 1
    return c
    

st1 = input('enter the string: ')
st2 = input('enter the string: ')

r = matches(st1,st2)
print(r)