import random

top = -1; items = [random.randint(1,100) for i in range(10)]
top = len(items)-1
print("Initial Stack : ", items); print("Currently Top = ", top)

items.append(21); top += 1
items.append(56); top += 1
print("After stack was added : ", items); print("Currently Top = ", top)

print("Stack is poped : ")
for i in range(13) : print(items.pop()); top -= 1
print("After stack was poped : ", items); print("Currently Top = ", top)