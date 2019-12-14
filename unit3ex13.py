""" Write a program that asks the user for a number and then
    prints out the sine, cosine, and tangent of that number """


import math

from math import sin, cos, tan

number = int(input(' enter a number '))

print('sinus of number is ',round(sin(number*math.pi/180),2))
print('cosinus of number is ',round(cos(number*math.pi/180),2))
print('tangent of number is ',round(tan(number*math.pi/180),2))
      
