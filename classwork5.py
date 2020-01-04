# decimal to binary  question : change  decimal 35 to binary
n = int(input('enter decimal'))
bi = []
for i in range (8):
    a = n//2
    b = n%2
    n = a
    bi = bi + [b]
bi.reverse() # 
print (bi)
