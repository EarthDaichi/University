import random

class Queue:
    def __init__(self):
        self.myQueue = []
        self.done = 0; self.count = 0; self.PushNo =1; self.PopNo = 1
    def addData(self, number):
        self.myQueue.append(number)
        self.count = len(self.myQueue)
        print(f"Push {self.PushNo}. myQueue = {self.myQueue}, Done = {self.done}, Count = {self.count}")
        self.PushNo += 1
    def getData(self):
        if(self.count >= 0):
            if(self.count == 0):
                self.done = 0; self.count = len(self.myQueue)
                print(f"Now, Done = {self.done}, Count = {self.count} and Queue is empty")
            else:
                Temp = self.myQueue[0]
                self.myQueue.pop(); self.done += 1
                print(f"Pop {self.PopNo}. Pop data = {Temp}, Done = {self.done}, Count = {self.count}, myQueue = {self.myQueue}")
                self.PopNo += 1; self.count = len(self.myQueue)
        else:
            print("Queue is empty")
    def Display(self):
        print(f"Currency, Done = {self.done}, and Count = {self.count}, myQueue = {self.myQueue}")

Q = Queue()
for i in range(20):Q.addData(random.randint(1,100))
Q.Display()
for i in range(random.randint(1,20)):Q.getData()
Q.Display()