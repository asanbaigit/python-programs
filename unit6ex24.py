""" In calculus, the derivative of x4 is 4x3. The derivative of x5 is 5x4. The derivative of x6 is 6x5. 
This pattern continues. Write a program that asks the user for input like x^3 or x^25 and prints the derivative. 
For example, if the user enters x^3, the program should print out 3x^2. """

t = input('enter expression ')
e = eval(t[2:])
print(e,t[:2],e-1,sep='')