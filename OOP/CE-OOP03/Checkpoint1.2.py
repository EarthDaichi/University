class ShapeCalculator:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
        self.pi = 3.14
class Area(ShapeCalculator):
    def CircleArea(self):
        return (2*self.pi*self.radius)
class Volume(ShapeCalculator):
    def SphereVolume(self):
        return (self.pi*self.radius*self.radius)
    def CylinderVolume(self):
        return (2*self.pi*self.radius*self.height)

A = Area(4,5)
B = Volume(7,9)
print(f"Circle Area = {A.CircleArea():.2f}")
print(f"Sphere Volume = {B.SphereVolume():.2f}")
print(f"Cylinder Volume = {B.CylinderVolume():.2f}")