t = input('Enter the string ')
r= []

l = t.split(' ')

for i in range (len(l)):
    temp = l[i].split(',')
    for j in range(len(temp)):
        r = r + [temp[j]]
print(r)
