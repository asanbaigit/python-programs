"""Write a program that gets a string from the user containing a potential telephone number. The program should print
Valid if it decides the phone number is a real phone number,and Invalid otherwise. A phone number is considered valid 
as long as it is written in the form abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number 
should contain only numbers and dashes, and the number of digits in each group must be correct. Test your program with 
the output shown below.
Enter a phone number: 1-301-447-5820 Valid 
Enter a phone number: 301-447-5820 Valid 
Enter a phone number: 301-4477-5820 Invalid 
Enter a phone number: 3X1-447-5820 Invalid 
Enter a phone number: 3014475820 Invalid """
p = input('Enter a number ')
flag = True
if p.count('-') < 2 or p.count('-')> 3:
    flag = False
else:
    nums = p.split('-')
    if len(nums) < 4:
        nums.insert(0,'1')
    if nums[0] != '1' or  not nums[0].isnumeric():
        flag = False
    if len(nums[1]) != 3 or  not nums[1].isnumeric():
        flag = False
    if len(nums[2]) != 3 or  not nums[2].isnumeric():
        flag = False
    if len(nums[3]) != 4 or  not nums[3].isnumeric():
        flag = False

if flag :
    print('Valid')
else :
    print ('invalid')
