""" Write a program that prints out the sine and cosine of the angles
    ranging from 0 to 345◦ in 15◦ increments. Each result should be
    rounded to 4 decimal places. Sample output is shown below:
    0 --- 0.0 1.0
    15 --- 0.2588 0.9659
    30 --- 0.5 0.866 ...
    345 --- -0.2588 0.9659 """

import math
from math import sin,cos,degrees

for i in range (0,350,15):
    print ('sin(',i,') = ',round(sin(i*math.pi/180),4),' and cos(', i ,') = ',round(cos(i*math.pi/180),4))


