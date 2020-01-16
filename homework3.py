""" Get  number from use and split number into digits using arithmetic operations, output each digit starting
from first digit line by line """

n = eval(input('Enter the number : '))

string = str(n)
i = 0
while i < len(string):
    print(int(string[i]))
    i += 1