"""  The number 99 has the property that if we multiply its digits together and then add the sum of its digits 
to that, we get back to 99. That is, (9×9)+(9+9) = 99. Write a program to ﬁnd all of the numbers less than
 10000 with this property. (There are only nine of them.) """
S = []
L = []
m = 0
s = 1

for i in range (22,23):
    
    for j in str(i):
            print(int(i[j]))
            
            