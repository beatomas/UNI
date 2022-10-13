
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance_origin(self):
        x_dis = (self.x)**2
        y_dis = (self.y)**2
        return (x_dis + y_dis)**0.5
    def distance(self,altre):
        x_disa = (self.x - altre.x)**2
        y_disa= (self.y - altre.y)**2
        return (x_disa + y_disa)**0.5
    def midpoint(self,altre):
        x_mid = (self.x + altre.x)/2
        y_mid = (self.y + altre.y)/2
        return Point(x_mid,y_mid)
    def slope(self,altre):
        x_sl = (self.x - altre.x)
        y_sl = (self.y + altre.y)
        return (y_sl/x_sl)
    def __str__(self):
        return ("("+str(self.x)+","+str(self.y)+")")
    
class Rectangle ():
    def __init__ (self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height
    def area(self):
        return (self.width*self.height)
    def perimeter(self):
        return (self.width*2 + self.height*2)
    def is_square(self):
        return (self.width == self.height)
    def zoom(self,z):
        self.width *= z
        self.height *= z
        return (self)
    def move(self,n1,n2):
        self.origin.x += n1
        self.origin.y += n2
        return (self)
    def get_vertex(self):
        llista = []
        llista.append(self.origin)
        P1 = Point(self.origin.x+self.width -1, self.origin.y)
        llista.append(P1)
        P2 = Point(self.origin.x+self.width -1, self.origin.y+self.height -1)
        llista.append(P2)
        P3 = Point(self.origin.x, self.origin.y+self.height -1)
        llista.append(P3)
        return (llista)
    def contains(self,p):
        return ((p.x >= self.origin.x) & (p.x <= (self.origin.x + self.width)) & (p.y >= self.origin.y) & (p.y <= self.origin.y + self.height))
    def overlap(self,R):
        if ((self.origin.x < R.origin.x) and (self.origin.y < R.origin.y)):
            x_left = max(self.origin.x,R.origin.x)
            y_top = max(self.origin.y,R.origin.y)
            R = Rectangle(Point(x_left,y_top),abs(self.width-R.width),abs(self.height-R.height))
            return (R)
        else:
            return False
        

        
        
        
        
        
        
        
    