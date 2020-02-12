"""
Write a function called verbose that, given an integer less than 10**15, returns the name of the integer in 
English. As an example, verbose(123456) should return one hundred twenty-three thousand, four hundred 
fifty-six. """

def evaluate_1000(L):
    for i in range (len(L)):
        if L[i] == 1000 and L[i+1] == 0:
            L[i+2] = 0


def evaluate_under_20(L):
    for i in range (len(L)):
        if L[i] == 100:
            if L[i+1] + L[i+2] < 20:
                L[i+1] = L[i+1] + L[i+2]
                L[i+2] = 0

def insert_and(L):
    for i in range (len(L)):
        if L[i] == 100:
            L.insert(i+1,-1)

def get_digits(n):
    L = []
    c = 0
    if n < 21:
        return [n]
    while n > 0:
        if c <= 1:
            L.append(n % 10 * 10 ** c)
        
        elif c == 2:
            L.append(10**c)
            L.append(n%10)
        else:
            L.append(10**c)
            c = -1
            n = n * 10
        n = n // 10
        c = c + 1
    L.reverse()
    evaluate_1000(L)
    evaluate_under_20(L)
    insert_and(L)

    return L

D = {-1: 'and',0: '', 1 : 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
    13: 'thirteen', 14: 'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40:'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand', 10000: 'ten thousand'
    }

n = eval(input('enter n: '))
L = get_digits(n)
print(L)

s = ''
for l in L:
    s = s + D[l] + ' '
print(s)