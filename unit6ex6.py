"""Write a program that asks the user to enter a string s and then converts s to lowercase, removes all the periods 
 and commas from s, and prints the resulting string """

s=input('enter a string ')
s=s.lower()
print(s)
s=s.replace('.',' ')
s=s.replace(',',' ')
print(s)