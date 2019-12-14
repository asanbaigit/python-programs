# One way to ﬁnd out the last two digits of a number is to mod the
# number by 100. Write a program that asks the user to enter a power.
# Then ﬁnd the last two digits of 2 raised to that power.

answer = int(input('enter a number '))
x=2

print (answer)
print (x**answer)
print ((x**answer)%100)
