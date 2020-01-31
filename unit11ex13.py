"""Suppose you are given the following list of strings: L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 
'acababba'] Patterns like this show up in many places, including DNA sequencing. The user has a string of their 
own with only some letters ﬁlled in and the rest as asterisks. An example is a**a****. The user would like to 
know which of the strings in the list ﬁt with their pattern. In the example just given, the matching strings 
are the ﬁrst and fourth. One way to solve this problem is to create a dictionary whose keys are the indices 
in the user’s string of the non-asterisk characters and whose values are those characters. Write a program 
implementing this approach(or some other approach)to ﬁnd the strings that match a user-entered string. """


L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba'] 
D = []
for w in L:
    D.append({i : w[i] for i in range (len(w))})
print (D)
q = input('Enter :')
K = {}
for i in range (len(q)):
    if q[i].isalpha():
        K[i]= q[i]
print(K)
for i in range(len(D)):
    c = 0
    for key in K:
        if K[key] == D[i][key]:
            c += 1
    if c == len(K):
        print(L[i])