class CQueue():
    def __init__(self,max):
        self.max = max
        self.myQueue = [0]*self.max
        self.front = self.rear = -1
        self.EnQNo = self.DeQNo = 0
    def Enqueue(self,number):
        if((self.front==0 and self.rear==self.max-1) or (self.front== self.rear+1)):
            print("This queue is full")
            return
        if(self.front==-1):
            self.front = 0; self.rear = 0
        else:
            if(self.rear == self.max-1):
                self.rear = 0
            else:
                self.rear = self.rear +1
        self.EnQNo = self.EnQNo+1
        self.myQueue[self.rear] = number
        print(f"Enqueue no {self.EnQNo}, front = {self.front}, rear = {self.rear}")
        print("Data =", self.myQueue)

    def Dequeue(self):
        if(self.front==-1):
            print("This Queue is empty")
            return
        if(self.front>self.rear):
            print("This Queue is empty")
            self.front = self.rear = -1
        if(self.front==0):
            self.DeQNo = self.DeQNo+1
            self.temp = self.myQueue[self.front]
            self.myQueue[self.front]=0
            self.front = self.front+1
            print(f"Dequeue no {self.DeQNo}, Dequeue = {self.temp}, front = {self.front}, rear = {self.rear}")
            print("Data =", self.myQueue)
        else:
            if(self.front==self.max):
                self.front = 0
            else:
                self.DeQNo = self.DeQNo+1
                self.temp = self.myQueue[self.front] = 0
                self.myQueue[self.front] = 0
                self.front = self.front+1
                print(f"Dequeue no {self.DeQNo}, Dequeue = {self.temp}, front = {self.front}, rear = {self.rear}")
                print("Data = ", self.myQueue)
Queue = CQueue(4)
Queue.Enqueue(10); Queue.Enqueue(20); Queue.Enqueue(30); Queue.Enqueue(40);
Queue.Dequeue();   Queue.Dequeue();   Queue.Dequeue();   Queue.Dequeue()