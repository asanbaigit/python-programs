'''
n = int(input('enter n'))
a = 0
for i in range (n):
    a = a + (n-i)*(10**i)
print(a)


n = int(input("enter n"))
for i in range(1,n+1):
    print(i, end = "")


n = int(input('enter the n'))
integer_list =tuple( map(int, input('enter the list').split()))
print(hash(integer_list))
'''
'''
n = int(input('enter n: '))
student_marks = {}
for _ in range(n):
    name, *line = input('enter name score student_marks: ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
#print(scores)
#print(name)
query_name = input('query_name')
print(float(sum(student_marks[query_name])/len(student_marks[query_name])))'''
"""
x = int(input('enter x '))
y = int(input('enter y '))
z = int(input('enter z '))
n = int(input('enter n '))
ans=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(ans)
"""
'''
for i in range(int(input('enter the n '))):
    name = input('enter the name ')
    score = float(input('enter the score '))
    l = [name,score]
    
print(L)

'''
"""
string = input('enter the string: ')
sub_string = input('enter the substring: ')
count = 0
for i in range (0,len(string)-len(sub_string)+1):
    if string[i:i+len(sub_string)] == sub_string:
        count +=1
print (count)"""
"""
def solve(s):
    s = s.split()
    l = ''
    for i in range (len(s)):
        l = l +' ' + s[i].capitalize()
    print (l)

s = (input('enter the name '))
solve(s)"""

"""

s = (input('enter the name '))
s = s.split()
p=s
print(p)
for i in range(len(p)):
    if(i==0 and p[i].isalpha()):
        p[i]=p[i].capitalize()
    elif(p[i].isspace() and p[i+1].isalpha()):
        p[i+1]=p[i+1].capitalize()
        #i+=1
    k="".join(p)
print(k)

ishtebedigo bu 
"""

t = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4

for i in range (0,len(t),4):
    print(t[i:i+w])

"""
N = input('enter the N: ')
s = set()
for i in range (int(N)):
    s.add(input('enter the y: '))
print(len(s))"""

