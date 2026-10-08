import random
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nav = Node(0)
    def addNode(self, data):
        new_node = Node(data)
        if(self.tail is None):
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def displayNode(self):
        nodes = []
        self.nav = self.head
        while(self.nav is not None):
            nodes.append(self.nav.data)
            self.nav = self.nav.next
        print("Double Linked-List : ", nodes)
    def displayNodeReverse(self):
        nodes = []
        self.nav = self.tail
        while(self.nav is not None):
            nodes.append(self.nav.data)
            self.nav = self.nav.prev
        print("Double Linked-List : ", nodes)
    def mySearch(self, what):
            search1 = self.head
            search2 = self.tail
            while(search1 and search2):
                if(search1.data == what):
                    print(f"Found {what} by head to tail")
                    break
                if(search2.data == what):
                    print(f"Found {what} by head to head")
                    break
                if(search1 == self.tail and search2 == self.head):
                    print("Not Found")
                    break
                search1 = search1.next
                search2 = search2.prev
    def deleteNode(self, target):
        self.nav = self.head
        while (self.nav != None):
            if self.nav.data == target:
                if self.nav.prev:
                    self.nav.prev.next = self.nav.next
                if self.nav.next:
                    self.nav.next.prev = self.nav.prev
                if self.nav == self.head:
                    self.head = self.nav.next
                return
            self.nav = self.nav.next

dll = DoubleLinkedList()
for i in range(1,21):
    dll.addNode(random.randint(1,100))
dll.displayNode()
dll.mySearch(58)
dll.displayNodeReverse()
for i in range(1,100):
    dll.deleteNode(random.randint(1,100))
dll.displayNode()
dll.mySearch(50)