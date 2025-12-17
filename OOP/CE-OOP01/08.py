import math

class CylinVol:
    def __init__(self,r,h):
        self.r = r
        self.h = h
    def CylinVolCal(self):
        vC = math.pi*self.r*self.r*self.h
        print(f"Cylindrical volume = {vC}")

print('This is cylindrical volume calculation program')
r = float(input("Enter radious : "))
h = float(input("Enter height : "))
ans = CylinVol(r,h)
ans.CylinVolCal()