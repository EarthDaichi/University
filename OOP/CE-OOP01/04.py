import math

print('This is cylindrical volume calculation program')
r = float(input("Enter radius : "))
h = float(input("Enter heigjht : "))
vC = math.pi*r*r*h
print(f"Cylindrical volume = {vC}")

print("This is spherical volume calculation program")
r = float(input("Enter radious : "))
vSP = 4/3*math.pi*r**3
print(f"Cylindrical volume = {vSP}")

print("This is spherical volume calculation program")
W = float(input("Enter wide : "))
L = float(input("Enter length : "))
H = float(input("Enter height : "))
vP = W*L*H/3
print(f"Pyramid volume = {vP}")