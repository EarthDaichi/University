
myQueue = []

front = 0
rear = -1

myQueue.append(10); rear += 1
print(f"Push 1. myQueue = {myQueue}, front = {front}, rear = {rear}")
myQueue.append(15); rear += 1
print(f"Push 2. myQueue = {myQueue}, front = {front}, rear = {rear}")
myQueue.append(20); rear += 1
print(f"Push 3. myQueue = {myQueue}, front = {front}, rear = {rear}")

if(front <= rear):
    myQueue.pop(0); front += 1
    print(f"Pop 1. myQueue = {myQueue}, front = {front}, rear = {rear}")
else:print("Queue is empty")
if(front <= rear):
    myQueue.pop(0); front += 1
    print(f"Pop 2. myQueue = {myQueue}, front = {front}, rear = {rear}")
else:print("Queue is empty")