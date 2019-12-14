
# Write a program that draws “modular rectangles” like the ones below. The user speciﬁes the
# width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
# from left to right and top to bottom, but are all done mod 10. Below are examples of a 3×5
# rectangle and a 4×8. 


height = int(input("Enter the height  : "))
width = int(input("Enter the width  : "))
counter = 0

for i in range(height*width):
        if counter == width :
                print()
                counter = 0
        print(i%10, end=' ')   # i % 10   important !!
        counter = counter+1
        
    
