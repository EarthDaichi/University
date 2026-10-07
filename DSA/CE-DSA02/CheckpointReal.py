import random
import CheckpointLib

aStack = CheckpointLib.Stack()
for i in range(20):aStack.push(random.randint(1,100))
print("Data in Stack : ", aStack.display())

print("Data Count =", aStack.count())

print("Check Top Data : ", aStack.check())

print("Check Random Data : ", aStack.check(15))

print("Pull Data :", aStack.pull())
print("Data Remaining : ", aStack.display())
print("Data Count = ", aStack.count())

print("Pull Random Data :", aStack.pull(13))
print("Data Remaining : ", aStack.display())
print("Data Count = ", aStack.count())

print("Data sum = ", aStack.sum())
print("Data min = ", aStack.min())
print("Data max = ", aStack.max())

print("Sorted Data : ", aStack.sort())
print("Reverse Sorted Data : ", aStack.sort(1))
print("Data in Stack : ", aStack.display())

print("Reversed Data : ", aStack.reverse())
print("Data in Stack : ", aStack.display())

print("Permanent Sorting : ", aStack.perma_sort())
print("Data in Stack : ", aStack.display())

print("Permanent Reverse : ", aStack.perma_reverse())
print("Data in Stack : ", aStack.display())
