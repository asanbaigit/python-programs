"""
 Write a function called change_case that given a string, returns a string with each upper case letter 
 replaced by a lower case letter and vice-versa. """

def change_case(st):
    s = ''
    for i in range (len(st)):
        if st[i].islower():
            s = s + st[i].upper()
        elif st[i].isupper():
            s = s + st[i].lower()
    return s

st = input('enter the string: ')
p = change_case(st)
print(p)

