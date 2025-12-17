import math

def CylinVolCal(r,h):
    vC = math.pi*r*r*h
    print(f"Cylindrical volume = {vC}")
def SphereVolCal(r):
    vSP = 4/3*math.pi*r**3
    print(f"Cylindrical volume = {vSP}")
def PyramidVolCal(W,L,H):
    vP = W*L*H/3
    print(f"Pyramid volume = {vP}")

ch ='y'
while ch != 'n':
    print('--- Welcome to Volume Calculation Program ---')
    print('Press 1: Cylindrical Volume Calculation')
    print('Press 2: Spherical Volume Calculation')
    print('Press 3: Pyramid Volume Calculation')
    print('---------------------------------------------')

    choice = int(input("Please, select calculation program : "))

    if choice == 1:
        print('This is cylindrical volume calculation program')
        r = float(input("Enter radius : "))
        h = float(input("Enter height : "))
        CylinVolCal(r,h)
    elif choice == 2:
        print("This is spherical volume calculation program")
        r = float(input("Enter radious : "))
        SphereVolCal(r)
    elif choice == 3:
        print("This is spherical volume calculation program")
        W = float(input("Enter wide : "))
        L = float(input("Enter length : "))
        H = float(input("Enter height : "))
        PyramidVolCal(W,L,H)
    else:
        print("Please, press 1 or 2 or 3")
    
    ch = input("Press any key to continue (n = terminate): ")