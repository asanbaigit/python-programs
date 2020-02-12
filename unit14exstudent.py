class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def print_student(self):
        print('name = ', self.name, ' age = ', self.age, ' id = ', self.id)
    
    def print_hello():
        print('Hello')

s1 = Student('Iron Man', 20, 1)
print(id(s1))
s1.print_student()
Student.print_hello()
s2 = Student('Batman', 30, 2)
print(id(s2))
s2.print_student()