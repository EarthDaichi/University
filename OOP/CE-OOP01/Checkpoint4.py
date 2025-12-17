import math

class MultiVolume:
    def CylinVolCal(self,r,h):
        self.r = r;self.h = h
        vC = math.pi*self.r*self.r*self.h
        print(f"Cylindrical volume = {vC}")
    def SphereVolCal(self,r):
        self.r = r
        vSP = math.pi*self.r**3
        print(f"Spherical volume = {vSP}")
    def PyramidVolCal(self,W,L,H):
        self.W = W, self.L = L, self.H = H
        vP = self.W*self.L*self.H/3
        print(f"Pyramid volume = {vP}")

ch = '1'
while ch != 'e':
    ans = MultiVolume()
    print('--- Welcome to Volume Calculation Program ---')
    print('Press 1: Cylindrical Volume Calculation')
    print('Press 2: Spherical Volume Calculation')
    print('Press 3: Pyramid Volume Calculation')
    print('---------------------------------------------')
    choice = int(input("Please, select calculating program: "))
    if choice == 1:
        print('This is Cylindrical volume calculation program')
        r = float(input("Enter radious: "))
        h = float(input("Enter height: "))
        ans.CylinVolCal(r,h)
    elif choice == 2:
        print('This is Spherical volume calculation program')
        r = float(input("Enter radious: "))
        ans.SphereVolCal(r)
    elif choice == 3:
        print('This is Cylindrical volume calculation program')
        W = float(input("Enter wide: "))
        L = float(input("Enter lenght: "))
        H = float(input("Enter height: "))
        ans.PyramidVolCal(W,L,H)
        
    ch = input("Enter to continue (Enter 'e' to terminate program)")