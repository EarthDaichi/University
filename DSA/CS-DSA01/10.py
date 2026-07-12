import random

data = [random.randint(1,100) for i in range(8)]

print("Data display before push")
print("Data : ", data)

data.append(15); data.append(67)

print("Data display after push")
print("Data : ", data)

data.pop(0)

print("Data : ", data)

data.pop(); data.pop(0); data.pop(2)
#        ในภาพตัวอย่างเป็น "data(2)" คาดว่าน่จะเป็น "data.pop(2)"
print("Data : ", data)