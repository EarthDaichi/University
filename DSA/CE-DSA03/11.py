myQueue = []
PushNo = 1; PopNo = 1; front = 0
def addData(number):
    global myQueue, PushNo, PopNo
    if(len(myQueue) < 10):
        myQueue.append(number)
        print(f"Push {PushNo}. myQueue = {myQueue}, Count of data = {len(myQueue)}")
        PushNo += 1
    else: print("Queue is full")
def getData():
    global myQueue, front, PushNo, PopNo
    if(len(myQueue) <= 0):
        print(f"Now, Count of data = {len(myQueue)} and Queue is empty")
    else:
        temp = myQueue[front]
        myQueue.pop(0); front += 1
        print(f"Pop {PopNo}. Pop data = {temp}, Count of Data = {len(myQueue)}, myQueue = {myQueue}")
        PopNo += 1
def Display():
    global myQueue, PushNo, PopNo
    print(f"Currently, myQueue = {myQueue}, Count of Data = {len(myQueue)}")

addData(2); addData(4); addData(8); addData(16); addData(32)
Display()
getData();getData();getData()
Display()