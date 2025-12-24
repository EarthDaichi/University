class BasicShape:
    def __init__(self,width,height,thick = 1):
        self.width = width
        self.height = height
        self.thick = thick
class Area(BasicShape):
    def CalculateArea(self):
        return (self.width*self.height)
class Cube(BasicShape):
    def CalculateCube(self):
        return (self.width*self.height*self.thick)
    
a = Area(14,15)
print('Area = ', a.CalculateArea())
c = Cube(3 , 7 , 9)
print('Volume = ', c.CalculateCube())