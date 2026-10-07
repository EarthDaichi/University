class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nav = Node(0)
    def addNode(self,data):
        if(self.tail is None):
            new_node = Node(data)
            if(self.tail is None):
                self.tial = new_node
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
        print("Double Linked-List : ",nodes)
    


dll = DoubleLinkedList()
dll.addNode(9); dll.addNode(18); dll.addNode(27)
dll.addNode(36); dll.addNode(45); dll.addNode(56); dll.addNode(67); dll.addNode(99)
dll.displayNode()