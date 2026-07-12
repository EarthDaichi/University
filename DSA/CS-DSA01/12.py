import random

dsa = [random.randint(1,200) for i in range(10)]
print(dsa)

dsb = dsa.copy()

result = sum(dsb)
print(f"ผลรวมทั้งหมด = {result}")