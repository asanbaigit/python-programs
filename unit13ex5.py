"""Write a function called first_diff that is given two strings and returns the ﬁrst location in which the
 strings differ. If the strings are identical, it should return -1. """

def first_diff (st1,st2):
    for i in range(min(len(st1),len(st2))):
        if st1[i] != st2[i]:
            return [i]
    return -1

st1 = input('enter the string')
st2 = input('enter the string')

r = first_diff(strg)
print(r)

