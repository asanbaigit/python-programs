"""  People often forget closing parentheses when entering formulas. Write a program that asks the user to enter 
a formula and prints out whether the formula has the same number of opening and closing parentheses."""

t=input('enter the formula ')

if t.count('(') != t.count(')'):
    print('Wrong expression')
else:
    print('Right expression')

