"""Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000."""

# L = [i for i in range(100,1000) if str(i)==str(i)[::-1]] 
L = [i for i in range(100,1000) if i == i%10*100 + i//10%10*10 + i//100%10] # the same without using string
print(L)
print('There are -',len(L),'palendroms between 100 and 1000')