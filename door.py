'''
n = input('enter the nums: ')
print(n)

L = list((n.split(' ')))
print(L)

for i in range ((int(L[0])//2)):
    print ('-'* int(L[1]))
print('-'*((int(L[1])//2)-3)+'WELCOME'+'-'*((int(L[1])//2)-3))
for j in range ((int(L[0])//2)):
    print ('-'* int(L[1]))
'''

N, M = map(int,input('enter the ').split())
for i in range(1,N,2): 
    print((i * ".|.").center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M,"-"))