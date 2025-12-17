import math

print('--- Welcome to Volume Calculation Program ---')
print('Press 1: Cylindrical Volume Calculation')
print('Press 2: Spherical Volume Calculation')
print('Press 3: Pyramid Volume Calculation')
print('Press 4: Square Volume Calculation')
print('Press 5: Cone Volume Calculation')
print('---------------------------------------------')

choice = int(input("Please, select calculation program : "))

if choice == 1:
    print('This is cylindrical volume calculation program')
    r = float(input("Enter radius : "))
    h = float(input("Enter heigjht : "))
    vC = math.pi*r*r*h
    print(f"Cylindrical volume = {vC}")

elif choice == 2:
    print("This is spherical volume calculation program")
    r = float(input("Enter radious : "))
    vSP = 4/3*math.pi*r**3
    print(f"Cylindrical volume = {vSP}")

elif choice == 3:
    print("This is spherical volume calculation program")
    W = float(input("Enter wide : "))
    L = float(input("Enter length : "))
    H = float(input("Enter height : "))
    vP = W*L*H/3
    print(f"Pyramid volume = {vP}")
elif choice == 4:
    print("This is square volume calculation program")
    W = float(input("Enter wide : "))
    L = float(input("Enter length : "))
    H = float(input("Enter height : "))
    vSq = W*L*H
    print(f"Square volume = {vSq}")
elif choice == 5:
    print("This is cone volume calculation program")
    r = float(input("Enter radious : "))
    h = float(input("Enter height : "))
    vC = 1/3*math.pi*r*r*h
    print(f"Square volume = {vC}")