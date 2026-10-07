class Stack:
    def __init__(self):
        self.Data = []    
        self.top = -1
    def push(self,NewD):
        self.Data.append(NewD)
        self.top += 1
    def pull(self,Index=None):
        if(self.top >= 0):
            self.top -= 1
            return self.Data.pop() if(Index == None) else self.Data.pop(Index)
        else:
            return "Stack is empty"
    def check(self,Index=None):
        if(self.top >= 0):
            return self.Data[self.top] if(Index == None) else self.Data[Index]
        else:
            return "Index is empty"
    def count(self):
        return self.top +1
    def display(self):
        return self.Data
    def sum(self):
        return sum(self.Data)
    def min(self):
        return min(self.Data)
    def max(self):
        return max(self.Data)
    def sort(self,way=0):
        return sorted(self.Data,reverse=way)
    def perma_sort(self,way=0):
        self.Data = sorted(self.Data,reverse=way)
        return self.Data
    def reverse(self):
        return self.Data[::-1]
    def perma_reverse(self):
        self.Data = self.Data[::-1]
        return self.Data