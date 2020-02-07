"""2. (a) Write a function called add_excitement that takes a list of strings and adds an exclamation point (!)
 to the end of each string in the list. The program should modify the original list and not return anything. 
 (b) Write the same function except that it should not modify the original list and should instead return a 
 new list. """

"""
#a)
def add_exc1(L):
    for i in range(len(L)):
        L[i] = L[i] + '!'
"""
#b)
def add_exc2(L):
    K = []
    for i in range(len(L)):
        K.append(L[i] + '!')
    return K
"""
#a)
M = ['Hello','Python']
print(M)
Z = add_exc1(M)
print(Z)
print(M)
"""
#b)
K = ['Iron','Man']
print(K)
D = add_exc2(K)
print(D)
print(K)