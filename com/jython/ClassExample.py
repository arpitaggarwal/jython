class Point:
  
    # Constructor of the class
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
   
    # The method which is called if print is applied to this object
    def __str__(self):
        return "x-value :" + str(self.x) + " y-value :" + str(self.y)
    
    # + Operator
    def __add__(self,other):
        p = Point()
        p.x = self.x+other.x
        p.y = self.y+other.y
        return p
    
    # * Operator
    def __mul__(self,other):
        p = Point()
        p.x = self.x*other.x
        p.y = self.y*other.y
        return p
        
p1 = Point(3,4)
p2 = Point(2,3)
p3 = Point(3,4)
print p1
print p1.y
print (p1+p2+p3) 
print (p1*p2*p3) 