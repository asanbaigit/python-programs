"""Write a simple quote-of-the-day program. The program should contain a list of quotes, and when the user runs the 
program, a randomly selected quote should be printed. """

l=['GOL','PAS','TEP','KAC']
from random import choice 
quot = choice(l)
print(quot)