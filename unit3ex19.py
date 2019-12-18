
# Write a program that draws “modular rectangles” like the ones below. The user speciﬁes the
# width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
# from left to right and top to bottom, but are all done mod 10. Below are examples of a 3×5
# rectangle and a 4×8. 


height = int(input("Enter the height  : "))
width = int(input("Enter the width  : "))

for i in range(height*width):
        if i%width == 0 :
                print()
        print(i%10, end=' ')  
        
  # Here is solution without 'IF'      
"""
h=8 'we can take input as well'
w=4 'we can take input as well'
c=0
for i in range(h):
    for j in range(w):
        print(c%10,end=' ')
        c=c+1
    print() """

 # Here is solution without if and only 1 for
"""
h=3
w=5

for i in range(h*w):
   cursor = (i%w+1)//w
   print(i%10,'\n'*cursor, end='')"""
 
