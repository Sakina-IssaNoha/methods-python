from re import A


class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        a=3.14*self.radius**2
        return a 
    
    def circumfrence(self):
        c=2*3.14*self.radius
        return c    
    
    
class Square:
    def __init__(self,side_a):
        self.side_a=side_a
        
    def area(self):
        a=self.side_a**self.side_a
        return a
        
    def perimeter(self):
        p=4*self.side_a   
        return p       
    
    
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        a=self.length*self.width
        return a       
    
    def perimeter(self):
        p=2*(self.length+self.width)
        return p
              
              
class Sphere:
    def __init__(self,radius): 
        self.radius=radius
        
    def surface_area(self):
        s=4*(3.14*self.radius**2)
        return s
    
    def volume(self):
        v=4/3*(3.14*self.radius**3)
        return v                