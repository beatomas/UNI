from math import sqrt

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    def distance_origin(self):
        return sqrt((self.x**2)+self.y**2)
    
    def distancia(self,p2):
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
    
    def midpoint(self,p2):
        x = (self.x + p2.x)/2
        y = (self.y + p2.y)/2
        return Point(x,y)
    def slope(self,p2):
        x = (self.x - p2.x)
        y = (self.y + p2.y)
        return (y/x)

class Poligon():
    def __init__(self,vertex):
        assert (len(vertex) > 2), "Nombre de vertex inferior a 3"
        self.vertex = vertex
    
    def __str__ (self):
        x = ""
        for i in range (len(self.vertex)):
            x = (x + str(self.vertex[i]))
        return x
    
    def add_point (self,punt):
        self.vertex.append(punt)
        
    def perimetre(self):
        P = 0
        per = 0
        for i in range (len(self.vertex)-1):
            per = per + Point.distancia(self.vertex[i],self.vertex[i+1])
        P = per + Point.distancia(self.vertex[i+1],self.vertex[0])
        
        return(P)
        
class Triangle (Poligon):
    def __init__(self,vertex = None):
        Poligon.__init__(self,vertex)
        assert (len(vertex) > 2), "Nombre de vertex diferent a 3"
    	self.vertex = vertex      
            
    def area (self):
        vertex1 = self.vertex[0]
        vertex2 = self.vertex[1]
        vertex3 = self.vertex[2]
        
        s = self.perimetre()/2
        
        costat1 = Point.distancia(vertex1,vertex2)
        costat2 = Point.distancia(vertex2,vertex3)
        costat3 = Point.distancia(vertex3,vertex1)
        
        suma = s*(s-costat1)*(s-costat2)*(s-costat3)
        
        return (suma**0.5)
    
    def add_point (self,punt_nou):
        raise Exception ("Un triangle te 3 vèrtex")
        
class Quadrilater (Poligon):
    def __init__(self,vertex = None):
        Poligon.__init__(self,vertex)
        assert (len(vertex) == 4), "Nombre de vertex diferent a 4"
        self.vertex = vertex
            
    def add_point (self,punt_nou):
        raise Exception ("Un quadrilater te 4 vèrtex")
    
    def area (self):
        b = 0
        h = 0
        
        vertex1 = self.vertex[0]
        vertex2 = self.vertex[1]
        vertex3 = self.vertex[2]
        
        b = Point.distancia(vertex1,vertex2)
        h = Point.distancia(vertex2,vertex3)
        a = b * h
        
        return a