"""
Write a program that uses a boolean ﬂag variable in determining whether two lists have any items in common."""

L1 = [1,2,3,4,5]
L2 = [5,6,7,8,10]

flag = False

for l in L1:
    if l in L2:
        flag = True

if flag:
    print('Yes')
else:
    print('No')