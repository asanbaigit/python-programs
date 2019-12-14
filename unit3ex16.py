""" Below is described how to ﬁnd the date of Easter in any year.
Despite its intimidating appearance,this is not a hard problem.
Note that [x] is the ﬂoor function, which for positive numbers just drops
the decimal part of the number. For instanceb3.14c= 3. The ﬂoor function
is part of the math module.
C = century (1900’s→C =19)
Y = year (all four digits)
m=(15+C−[C/4]−[8C+13/25]) mod 30
n=(4+C−[C/4]) mod 7
a = Y mod 4
b = Y mod 7
c = Y mod 19
d =(19c+m) mod 30
e =(2a+4b+6d +n) mod 7
Easter is either March(22+d+e) or April(d+e−9). There is an exception if
d =29and e =6. In this case, Easter falls one week earlier on April 19.
There is another exception if d = 28, e = 6, and m = 2,5,10,13,16,21,24, or 39.
In this case, Easter falls one week earlier on April 18.
Write a program that asks the user to enter a year and prints out
the date of Easter in that year. """
