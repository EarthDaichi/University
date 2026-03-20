import random
import statistics

myData = [random.randint(1,100) for i in range(20)]

SD = statistics.stdev(myData)
print("Standard Deviation = ", SD)