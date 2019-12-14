# Write a program that generates a random number between 1 and 10
# and prints your name that many times.


from random import randint
x = randint(1,10)
name = input ('enter your name: ')
for i in range(x):
    print(x,i+1,name)
