""" HW1: Given a list of ints, print True if the array contains a 5 next to a 5 anywhere in the list. 
If no consecutive 5s or no 5s are detected then print False.

nums -> [1,5,5,1,1] -> True
nums -> [1,2,3] -> False
nums -> [1,8,5,5,1,0,-1] -> True
nums -> [1,4,4,1,99,99,4,3] -> False"""
'''nums = eval(input('enter a list '))
count = 0

if 5 not in nums:
    print('false')

for n in nums:
    if n == 5:
        count= count + 1

if count == 2:
    for i in range ((len(nums))-1):
        if nums[i]==5 and nums[(i+1)]==5:
            print('true')

else:
    print('false')'''
        
l = eval(input('Enter numbers: '))

flag = False

for i in range(1, len(l)):
    if l[i] == l[i-1] and l[i]==5:
        flag = True

print(flag)
