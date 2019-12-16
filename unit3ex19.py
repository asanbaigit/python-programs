
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
        
        

