num = eval(input('Enter the number : '))
actn = num = abs(num)
res = 0

while num > 0:
    dig = num % 10
    num = num // 10
    res = res *10 + dig

if res == actn :
    print('Palendrom')
else:
    print ('Not palendrom')