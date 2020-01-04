max1=max2=-1
min1=min2=101
total=0
flag=0
for i in range(10):
    score=eval(input('enter the socre '))
    if max1 < score:
        max2 = max1
        max1 = score
    elif max2 < score and max2 < max1:
        max2 = score
    if min1 > score:
        min2 = min1
        min1 = score
    elif min2 > score and min2 > min1:
        min2 = score
    if score < 0 or score > 100:
        flag = 1
    total = total + score

if flag == 1:
    print('score must be between 0 and 100')
else:
    print('max1', max1)
    print('max2',max2)
    print('min1',min1)
    print('min2',min2)
    print('average',total/10)
    print('average without min two scores',(total-min1-min2)/8)