import random

listA = [random.randint(1,50) for i in range(20)]
print(listA)
result = sum(listA)
print("Summation of listA = ", result)