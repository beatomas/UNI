

class Equip():
    def __init__(self,nom,ciutat,punts,pressupost):
        self.N = nom
        self.C = ciutat
        self.P = punts
        self.Pr = pressupost
        
    def __str__(self):
        return("Equip: "+str(self.N)+" "+str(self.C)+" "+str(self.P)+" "+str(self.Pr))
        
    def __lt__(self,altre):
        return(self.P < altre.P)
        
    def __gt__(self,altre):
        return(self.P > altre.P)
        
    def __le__(self,altre):
        return(self.P <= altre.P)
        
    def __ge__(self,altre):
        return(self.P >= altre.P)
        
    def __ne__(self,altre):
        return(self.P != altre.P) 
        
    def __eq__(self,altre):
        return(self.P == altre.P)
        
e1 = Equip("Barça","Barcelona",10,40)
e2 = Equip("Madrid","Madrid",8,30)
print(e1)
print(e2)
print(e1.__lt__(e2))
print(e1.__gt__(e2))
print(e1.__le__(e2))
print(e1.__ge__(e2))
print(e1.__ne__(e2))
print(e1.__eq__(e2))

