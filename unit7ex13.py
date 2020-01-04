"""Write a program that removes any repeated items from a   list so that each item appears at most once. 
For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]."""

l = eval(input('Enter sequence: '))

l2 = []

for num in l:
    #if l2.count(num) == 0:
    if num not in l2:
        l2.append(num)

print(l2)