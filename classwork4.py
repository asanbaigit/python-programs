####
t='Hello'
str =''
for i in range(len(t)):
    str=str+t[i]*2
print(str)

#Elvis
t='Elvis'
for i in range(len(t)):
    print(t[:i+1])

####
n='3.14159'
print(n[n.index('.')+1:])
print(n[2:])

####
t=input('enter text')
t2=t[::-1]
if t==t2:
    print ('Paledrom')
else:
    print ('not palendrom')
