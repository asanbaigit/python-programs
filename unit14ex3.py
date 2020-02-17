"""
Write a class called Password_manager. The class should have a list called old_passwords that holds all of
the user’s past passwords. The last item of the list is the user’s current password. There should be a 
method called get_password that returns the current password and a method called set_password that sets 
the user’s password. The set_password method should only change the password if the attempted password 
is different from all the user’s past passwords. Finally, create a method called is_correct that receives
a string and returns a boolean True or False depending on whetherthe string is equal to the current 
password or not. """

class PasswordManager:
    def __init__(self, old_passwords = []):
        self.old_passwords = old_passwords
    
    def __str__(self):
        return ','.join(self.old_passwords)

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, curr):
        if curr not in self.old_passwords:
            self.old_passwords.append(curr)

    def is_correct(self, q):
        return self.old_passwords[-1] == q

p = PasswordManager()
p .set_password('Iloveu')
print(p)

p = PasswordManager(['123','12345','qwerty'])
print(p.get_password())
print(p)

p.set_password('Iloveu')
print(p)

print(p.get_password())
p.set_password('123')
print(p)

print(p.is_correct('123'))
print(p.is_correct('Iloveu'))
