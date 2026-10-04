class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

llist = LinkedList()
llist.insertAtBegin(7)
llist.insertAtBegin(1)
llist.insertAtBegin(3)
llist.insertAtBegin(2)

print("Original Linked List:")
llist.printList()

llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()

llist.insertAtBegin(6)
llist.insertAtBegin(4)
llist.insertAtBegin(8)
llist.deleteNode(3)
llist.deleteNode(2)
print("\n------")
llist.printList()