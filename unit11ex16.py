"""
 (a) Write a program that converts Roman numerals into ordinary numbers. Here are the conversions: M=1000, 
 D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things like IV being 4 and XL being 40. 
 (b) Write a program that converts ordinary numbers into Roman numerals """
# a
romannum = input('Enter the roman number : ')
romannum = romannum.replace('IV','O')
romannum = romannum.replace('IX','P')
romannum = romannum.replace('XL','Q')
romannum = romannum.replace('XC','R')
romannum = romannum.replace('CD','S')
romannum = romannum.replace('CM','T')

D = {'I':1,'O':4,'V':5,'P':9,'X':10,'Q':40,'L':50,'R':90,'C':100,'S':400,'D':500,'T':900,'M':1000}

num = 0
for l in romannum:
    num = num + D[l]
print(num)

# b

nom = eval(input('Enter the number : '))
L = [1000,500,100,50,10,5,1]
F = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C',
     500: 'D', 1000:'M'}
Q = {}
while nom > 0:
    c = nom//L[0]
    nom = nom % L[0]
    Q[L[0]] = c
    del L[0]

res = ''
for key in Q:
    res = res + F[key]*Q[key]

res = res.replace('IIII','IV')
res = res.replace('VIV','IX')
res = res.replace('XXXX','XL')
res = res.replace('LXL','XC')
res = res.replace('CCCC','CD')
res = res.replace('DCD','CM')
print(res)


