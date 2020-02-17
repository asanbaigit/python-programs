import math

def convert_to_octal(n):
    r = 0
    c = 0
    while n > 0:
        d = n%8
        r = r + d*10**c
        n = n // 8
        c = c + 1
    return r

def convert_to_hex(n):
    D = {10: 'A', 11: 'B', 12: 'C', 13:'D', 14:'E', 15:'F'}
    s = ''
    while n > 0:
        d = n%16
        if d >= 10:
            s = D[d] + s[0:]    
        else:
            s = str(d) + s[0:]
        n = n // 16
    return s

def convert_to_bin(n):
    s = ''
    while n > 0:
        d = n%2
        s = str(d) + s[0:]
        n = n // 2
    return s

n = eval(input('enter n: '))
l = int(math.log2(n))+2
for i in range(1, n+1):
    s = ''
    f = '{:'+str(l)+ 'd}'
    s = s + f.format(i)
    s = s + f.format(convert_to_octal(i))
    f2 = '{:>'+str(l)+ 's}'
    s = s + f2.format(convert_to_hex(i))
    s = s + f2.format(convert_to_bin(i))
    print(s)