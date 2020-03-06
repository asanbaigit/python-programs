from math import sqrt
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x = '+ str(self.x) +', y = '+ str(self.y)

    def calc_dist(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calc_per(self):
        return self.p1.calc_dist(self.p2) + self.p2.calc_dist(self.p3) + self.p1.calc_dist(self.p3)

x,y = map(int,input('enter x y ').split())
p1 = Point(x,y)
x,y = map(int,input('enter x y ').split())
p2 = Point(x,y)
x,y = map(int,input('enter x y ').split())
p3 = Point(x,y)

t = Triangle(p1,p2,p3)

print(t.calc_per())

