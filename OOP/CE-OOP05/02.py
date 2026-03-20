import random
myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " ")

sum = 0
for i in myData:
    sum = sum+i
print("\nSummation = ", sum)