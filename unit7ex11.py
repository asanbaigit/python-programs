"""Using a for loop,create the list below, which consists of ones separated by increasingly many zeroes.
  The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]"""

res=[]
for i in range (11):
    res = res + [1]
    res = res + [0]*i
print(res)