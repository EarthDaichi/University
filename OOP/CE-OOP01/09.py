import math
class MultiVolume:
    def __init__(self,r,h,W,L,H):
        self.r = r; self.h = h; self.W = W; self.L = L; self.H = H
    def CylinVolCal(self):
        vC = math.pi*self.r*self.r*self.h; print(f"Cylindrical volume = {vC}")
    def SphereVolCal(self):
        vSP = 4/3*math.pi*self.r**3; print(f"Spherical volume = {vSP}")
    def PyramidVolCal(self):
        vP = self.W*self.L*self.H/3; print(f"Pyramid volume = {vP}")

r = float(input("Enter radious : ")); h = float(input("Enter height : "))
W = float(input("Enter wide: ")); L = float(input("Enter length: "))
H  =float(input("Enter height: "))
ans = MultiVolume(r,h,W,L,H)
print('This is cylindrical volume calculation program')
ans.CylinVolCal()
print("This is spherical volume calculation program")
ans.SphereVolCal()
print("This is pyramid volume calculation program")
ans.PyramidVolCal()