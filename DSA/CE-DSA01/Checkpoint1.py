import random

listA = [random.randint(1,100) for i in range(20)]
print(f"listA = {listA}")
listAA = sorted(listA)
listAB = sorted(listA,reverse=1)
print(f"Sorted listA = {listAA}")
print(f"Reverse Sorted listA = {listAB}")