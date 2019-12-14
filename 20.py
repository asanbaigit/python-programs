h = int(input("Enter the h  : "))
w = int(input("Enter the w  : "))
counter=0

for i in range(h*w):
        if counter == w :
                print()
                counter = 0
        print('*', end='')
        counter=counter+1
        
    
