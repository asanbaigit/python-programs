lines = [line.strip() for line in open('wordlist.txt')]
#a)
"""
c=0
for line in lines:
    if line[-3:] == 'ime':
        c = c + 1
        print(line)
print(c)

#b)

c=0
for line in lines:
    if line[1:4] == 'ave':
        c = c + 1
        print(line)
print(c)

#e)

c=0
v = 'aeiou'
for line in lines:
    flag = True
    for l in v:
        if l in line:
            flag = False
    if flag:
        print(line)
        c = c + 1

print(c)

#f)

c=0
v = 'aeiou'
for line in lines:
    flag = True
    for l in v:
        if l not in line:
            flag = False
    if flag:
        print(line)
        c = c + 1

print(c)

#g)

c=0
for line in lines:
    if len(line) == 7 or len(line) > 10:
        print(line)
        c = c + 1

print(c)

#h)

m = lines[0]
for i in range(1, len(lines)):
    if len(m) < len(lines[i]):
        m = lines[i]
print(m, len(m))

#i)

for l in lines:
    if l == l[::-1]:
        print(l)

#j,k

D = {}
for l in lines:
    if l != l[::-1]:
        D[l]=l

K = {}
for key in D:
    if key[::-1] in D:
        if key[::-1] not in K: #comment for solution of j
            K[key] = key[::-1]

print(K)
print(len(K))

#l)

for l in lines:
    flag = False
    if l[-3:] != 'lly':
        for i in range(1, len(l)):
            if l[i] == l[i-1]:
                flag = True
                break
        if flag:
            print(l)

#n)

for l in lines:
    if 'zu' in l:
        print(l)

#o)

for l in lines:
    c = 0
    for i in range(len(l)-1):
        if l[i:i+2] == 'ab':
            c = c + 1
    if c > 1:
        print(l)
"""
#p)

v = 'aeiou'
for l in lines:
    if len(l) > 5:
        c = 0
        for i in range(len(l)):
            if l[i] in v:
                c = c + 1
        if c >= 4:
            print(l)

#v)
'''
for l in lines:
    if len(l) > 6:
        if 'a' in l and 'b' in l and 'c' in l and 'd' in l and 'e' in l and 'f' in l:
            print(l)
'''
#w,x)
'''
for l in lines:
    if len(l) >= 8:
        #if l[:4] == l[-4:]: -> w
        if l[:4] == l[::-1][:4]:
            print(l
'''
#y)
'''
D = {}
v = 'aeiou'
for l in lines:
    if len(l) == 3 and l[0] not in v and l[2] not in v and l[1] in v:
        if l[0]+l[2] not in D: 
            D[l[0]+l[2]] = [l]
        else:
            D[l[0]+l[2]] = D[l[0]+l[2]] + [l]
for key in D:
    if len(D[key]) >= 5:
        print(D[key])
'''
#z)
"""
m = ''
m2 = ''
m3 = ''
for l in lines:
    if l.count('i') > m.count('i'):
        m3,m2,m = m2,m,l
print(m)
print(m2)
print(m3)
"""
        

        

    

