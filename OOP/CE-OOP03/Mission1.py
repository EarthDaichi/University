class ShapeCalculator:
    def __init__(self,width,height,thick = 1):
        self.width = width
        self.height = height
        self.thick = thick
    def CalculateArea(self):
        return (self.width*self.height)
    def CalculateVolume(self):
        return (self.width*self.height*self.thick)
    
a = ShapeCalculator(14,15)
print('Area = ', a.CalculateArea())
c = ShapeCalculator(3 , 7 , 9)
print('Volume = ', c.CalculateVolume())