max = 8
myQueue = [0]*max
front = rear = -1
EnQNo = DeQNo = 0
def Enqueue(number):
    global myQueue,front,rear,EnQNo,DeQNo
    if((front==0 and rear==max-1) or (front== rear+1)):
        print("This queue is full")
        return
    if(front==-1):
        front = 0; rear = 0
    else:
        if(rear == max-1):
            rear = 0
        else:
            rear = rear +1
    EnQNo = EnQNo+1
    myQueue[rear] = number
    print(f"Enqueue no {EnQNo}, front = {front}, rear = {rear}")
    print("Data =", myQueue)

def Dequeue():
    global myQueue, front, rear, EnQNo, DeQNo
    if(front==-1):
        print("This Queue is empty")
        return
    if(front>rear):
        print("This Queue is empty")
        front = rear = -1
    if(front==0):
        DeQNo = DeQNo+1
        temp = myQueue[front]
        myQueue[front]=0
        front = front+1
        print(f"Dequeue no {DeQNo}, Dequeue = {temp}, front = {front}, rear = {rear}")
        print("Data =", myQueue)
    else:
        if(front==max):
            front = 0
        else:
            DeQNo = DeQNo+1
            temp = myQueue[front] = 0
            myQueue[front] = 0
            front = front+1
            print(f"Dequeue no {DeQNo}, Dequeue = {temp}, front = {front}, rear = {rear}")
            print("Data = ", myQueue)

Dequeue();