s = "abcdefg"

print len(s)
print s
print s[0:4]

#TypeError: cannot concatenate 'str' and 'int' objects
print s+str(10)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "x-value" + str(self.x) + " y-value" + str(self.y)
    def __add__(self,other):
        p = Point()
        p.x = self.x+other.x
        p.y = self.y+other.y
        return p
        
p1 = Point(3,4)
p2 = Point(2,3)
p3 = Point(3,4)
print p1
print p1.y
print (p1+p2+p3) 
