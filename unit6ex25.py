"""In algebraic expressions,the symbol for multiplicationis often left out,as in 3x+4y or 3(x+5). Computers prefer those 
expressions to include the multiplication symbol, like 3*x+4*y or 3*(x+5). Write a program that asks the user for an 
algebraic expression and then inserts multiplication symbols where appropriate."""

t=input('enter a algebraic expression ')
result = ""
for i in range (len(t)):
    if t[i].isalpha():
        result = result + '*'
        result = result + t[i]
    else:
        result = result + t[i]
    #if t[i]=='(':
     #   result = result + '*'
      #  result = result + t[i]
    #else:
     #   result = result + t[i]

print(result)

       
        

        