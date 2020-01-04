"""Write a program that asks the user for a large integer and inserts commas into it according to the standard 
American convention for commas in large numbers. For instance, if the user enters 1000000, 
the output should be 1,000,000."""

n=eval(input('enter big int '))
# print("{:,}".format(n)) this is the shortest answer actually

s = str(n)
q = ''
if len(s)<4:
    q = s
    print(s)
if 3 < len(s) < 7:
    q =  s[:-3]+',' + s[-3:]
    print(q)
if 6 < len(s) < 10:
    q = s[:-6] + ',' + s[-6:-3]+ ',' + s[-3:]
    print(q)

