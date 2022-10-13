

class Point():
    def __init__(self,x,y):
        self.Cx = x
        self.Cy = y
    def distance_origin(self):
        x_dis = (self.Cx)**2
        y_dis = (self.Cy)**2
        return (x_dis + y_dis)**0.5
    def distance(self,altre):
        x_disa = (self.Cx - altre.Cx)**2
        y_disa= (self.Cy - altre.Cy)**2
        return (x_disa + y_disa)**0.5
    def midpoint(self,altre):
        x_mid = (self.Cx + altre.Cx)/2
        y_mid = (self.Cy + altre.Cy)/2
        return Point(x_mid,y_mid)
    def slope(self,altre):
        x_sl = (self.Cx - altre.Cx)
        y_sl = (self.Cy + altre.Cy)
        return (y_sl/x_sl)
    def __str__(self):
        return ("("+str(self.Cx)+","+str(self.Cy)+")")
        
p1 = Point(4,5)
p2 = Point(1,1)
print(p1)
print(p2)
print(p1.distance_origin())
print(p1.distance(p2))
print(p1.midpoint(p2))
print(p1.slope(p2))

"""

from math import sqrt

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    def distance_origin(self):
        return sqrt((self.x**2)+self.y**2)
    
    def distance(self,p2):
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
    
    def midpoint(self,p2):
        x = (self.x + p2.x)/2
        y = (self.y + p2.y)/2
        return Point(x,y)
    def slope(self,p2):
        x = (self.x - p2.x)
        y = (self.y + p2.y)
        return (y/x)
        
"""

