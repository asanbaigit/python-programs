"""
 Write a function called one_away that takes two strings and returns True if the strings are of the same 
 length and differ in exactly one letter, like bike/hike or water/wafer. """

def one_away(st1, st2):
    if len(st1) != len(st2):
        return False
    c = 0    
    for i in range (len(st1)):
        if st1[i] != st2[i]:
            c = c + 1
    if c == 1:
        return True
    return False

st1 = input('enter st1: ')
st2 = input('enter st2: ')

print(one_away(st1,st2))