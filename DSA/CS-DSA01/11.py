import random

dsa = [random.randint(1,200) for i in range(10)]
print(dsa)

dsb = dsa.copy()
print(dsb)
dsc = dsa[:]
print(dsc)
dsd = list(dsa)
print(dsd)