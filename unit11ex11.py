""" In Section 6.10 we met the substitution cipher. This cipher replaces every letter with a different letter.
 For instance every a might be replaced with an e, every b might be replaced with an a, etc. Write a program that 
 asks the user to enter two strings. Then determine if the second string could be an encoded version of the ﬁrst 
 one with a substitution cipher. For instance, CXYZ is not an encoded version of BOOK because O got mapped to 
 two separate letters. Also,CXXK is not an encoded version of BOOK,because K got mapped to itself. On the other 
 hand, CXXZ would be an encoding of BOOK. This problem can be done with or without a dictionary. """

mes = input('enter message:')
encr = input('enter encr:')

D = {}
flag = True
for i in range(len(mes)):
    c = 0
    if mes[i] not in D:
        D[mes[i]] = encr[i]
        c += 1
    if encr[i] not in D:
        D[encr[i]] = mes[i]
        c += 1

    if c == 1: 
        flag = False
        break
        
print(D)
if flag:
    print('Yes')
else:
    print('No')

        