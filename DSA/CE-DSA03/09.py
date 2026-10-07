myQueue = []
front = 0; rear = -1; PushNo = 1; PopNo = 1
def addData(number):
    global myQueue, front, rear, PushNo, PopNo
    myQueue.append(number)
    rear += 1
    print(f"Push {PushNo}. myQueue = {myQueue}, front = {front}, rear = {rear}")
    PushNo += 1
def getData():
    global myQueue, front, rear, PushNo, PopNo
    if(front >= 0):
        if(front > rear):
            front = 0; rear = -1; print(f"Now, front = {front}, rear = {rear} and Queue is empty")
        else:
            temp = myQueue[front]
            myQueue.pop(0); front += 1
            print(f"Pop {PopNo}. Pop data = {temp}, front = {front}, rear = {rear}, myQueue = {myQueue}")
            PopNo += 1
    else:print("Queue is empty")
def Display():
    global myQueue, front, rear, PushNo, PopNo
    print(f"Currently, myQueue = {myQueue}, front = {front} and rear = {rear}")

addData(70)
addData(80)
addData(90)
Display()
getData()
Display()