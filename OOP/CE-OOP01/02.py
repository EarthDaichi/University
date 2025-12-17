import math

def CylinVolCal(R, H):
    v = math.pi*R*R*H
    print(f"Cylidrical volme = {v}")

print('This is cylindrical vlume calculation program')
r = float(input("Enter radius : "))
h = float(input("Enter height : "))
CylinVolCal(r, h)