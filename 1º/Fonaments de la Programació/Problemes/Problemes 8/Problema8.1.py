
class Fraccio():
    def __init__(self,x,y):
        self.Num = x
        self.Den = y
        
    def __str__(self):
        return(str(self.Num)+"/"+str(self.Den))
        
    def __add__(self,altre):
        Den = (self.Den * altre.Den)
        Num = (self.Num * altre.Den + altre.Num * self.Den)
        return(Fraccio(Num,Den))
        
    def __sub__(self,altre):
        Den = (self.Den * altre.Den)
        Num = (self.Num * altre.Den - altre.Num * self.Den)
        return(Fraccio(Num,Den))
        
    def frac2float(self):
        return(self.Num/self.Den)
        
    def inv(self):
        return(Fraccio(self.Den,self.Num))