import random

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    def size(self):
        return len(self.items)
    def display(self):
        return self.items


stack = Stack()
for i in range(20): stack.push(random.randint(1,100))
print("Stack after pushing random number: ", stack.display())
print("Top element : ", stack.peek())
for i in range(3) : print("Popped element : ", stack.pop())
print("Stack after popping elements : ", stack.display())
print("Is stack empty? ", "Yes." if(stack.is_empty()) else "No.")
print("Size of stack : ", stack.size())