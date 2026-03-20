import random

myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " ")

sum = sum(myData)
print("\nSummation = ", sum)

avg = sum/len(myData)
print("Average = ", avg)

max = max(myData)
print("Maximum = ", max)

min = min(myData)
print("minimum = ", min)