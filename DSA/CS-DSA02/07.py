import random
top = -1
items = []

def Push(number):
    global items, top
    top += 1
    items.append(number)
def Pop():
    global items, top
    if(top > -1):
        print("items is popped =", items.pop())
        top -= 1
    else:
        print("items is empty")

items = [random.randint(1,100) for i in range(10) ]
top = len(items)-1
print("Initial items as ", items)
print("Currently Top = ", top)
for i in range(12):Pop()
print("Currently items as ", items)
print("Currently Top = ", top)