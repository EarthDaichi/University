class ShapeCalculator:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
        self.pi = 3.14
    def CircleArea(self):
        return (2*self.pi*self.radius)
    def SphereVolume(self):
        return (self.pi*self.radius*self.radius)
    def CylinderVolume(self):
        return (2*self.pi*self.radius*self.height)

A = ShapeCalculator(4,5)
print(f"Circle Area = {A.CircleArea():.2f}")
print(f"Sphere Volume = {A.SphereVolume():.2f}")
print(f"Cylinder Volume = {A.CylinderVolume():.2f}")