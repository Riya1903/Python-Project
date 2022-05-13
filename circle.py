
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
c1=circle(5)
c1.area()
c1.circumference()
print("area of circle= ",c1.area())
print("circumference of circle= ",c1.circumference())
