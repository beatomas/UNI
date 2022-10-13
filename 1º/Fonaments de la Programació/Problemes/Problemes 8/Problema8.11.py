
from math import sqrt
from math import cos
from math import sin


class Point2D():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_x(self):
        return (self.x)
    def get_y(self):
        return (self.y)
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def distancia(self,altre):
        x_disa = (self.x - altre.x)**2
        y_disa= (self.y - altre.y)**2
        return (x_disa + y_disa)**0.5
    def __str__(self):
        return ("("+str(self.x)+","+str(self.y)+")")

class Point3D(Point2D):
    def __init__(self,x,y,z):
        Point2D.__init__(self,x,y)
        self.z = z
    def get_x(self):
        return (self.x)
    def get_y(self):
        return (self.y)
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def get_z(self):
        return (self.z)
    def set_z(self,z):
        self.z = z
    def distancia(self,altre):
        x_1 = self.z * cos(self.y)*sin(self.x)
        y_1 = self.z * cos(self.y)
        z_1 = self.z * cos(self.y)*sin(self.x)
        
        x_2 = altre.z * cos(altre.y)*sin(altre.x)
        y_2 = altre.z * cos(altre.y)
        z_2 = altre.z * cos(altre.y)*sin(altre.x)
        d = sqrt(((x_2-x_1)**2)+((y_2-y_1)**2)+((z_2-z_1)**2))
        return d
    
    def __str__(self):
        return ("("+str(self.x)+","+str(self.y)+","+str(self.z)+")")
    
    
    
    
    
    
    
    
    
    
    