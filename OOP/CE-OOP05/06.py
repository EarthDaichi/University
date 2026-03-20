import random
import math

myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " ")

mySum = sum(myData)
print("\nSummation = ", mySum)

myMean = mySum/len(myData)
print("Average = ",myData)

max = max(myData)
print("Maximum = ", max)

min = min(myData)
print("Minimum = ", min)

myVariance = sum((x-myMean)**2 for x in myData)/len(myData)
print("Variance = ", myVariance)

SD = math.sqrt(myVariance)
print("Standard Deviation = ", SD)