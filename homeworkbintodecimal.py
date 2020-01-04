""" HW2: Given a list of 8 ints [0,1] convert the list into decimal representation of a number
[0, 0, 1, 0, 0, 0, 1, 1] -> 35
[0, 0, 0, 0, 0, 1, 1, 1] -> 7
[1, 1, 1, 1, 1, 1, 1, 1] -> 155  """

dec = 0
dec1 = 0
dec2 = 0
l1=[0, 0, 1, 0, 0, 0, 1, 1]
l2=[0, 0, 0, 0, 0, 1, 1, 1]
l3=[1, 1, 1, 1, 1, 1, 1, 1]

l1.reverse()
l2.reverse()
l3.reverse()

for i in range (8):
    dec=dec+(l1[i]*(2**i))
    dec1=dec1+(l2[i]*(2**i))
    dec2=dec2+(l3[i]*(2**i))
print(dec,dec1,dec2)

""" solution by teacher 
l = eval(input('Enter a list: '))

res = 0
for i in range(len(l)-1, -1, -1):
    res = res + l[i]*2**(7-i)
    #print(l[i], 2, (7-i))

print(res)"""