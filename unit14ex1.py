"""
Write a class called Investment with ﬁelds called principal and interest. The constructor should set
the values of those ﬁelds. There should be a method called value_after that returns the value of the
investment after n years. The formula for this is p(1+i)n, where p is the principal, and i is the 
interest rate. It should also use the special method __str__ so that printing the object will result
in something like below:
Principal - $1000.00, Interest rate - 5.12% """

class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest
    
    def __str__(self):
        s = ''
        s = s + 'Principal - $' + str(self.principal)
        s = s + ', Interest rate - ' + str(self.interest) + '%'
        return s
    
    def value_after(self, n):
        return self.principal * (1 + self.interest)**n
    
i = Investment(1000.0, 5.12)
print(i)
print(i.value_after(2))

