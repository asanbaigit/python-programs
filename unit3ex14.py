"""  Write a program that asks the user to enter an angle in degrees and
     prints out the sine of that angle """

import math

from math import sin

angle = int(input(' enter an angle in degrees '))


print ('sinus of an angle is ',round(sin(angle*math.pi/180),2))

