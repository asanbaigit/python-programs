"""
Write a function called is_sorted that is given a list and returns True if the list is sorted and 
False otherwise. """

def is_sorted(L):
    for i in range (1,len(L)):
        if L[i] - L[i-1] < 0 :
            return False
    return True
    

L = eval(input('Enter list: '))
print(is_sorted(L))
