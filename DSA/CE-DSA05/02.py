class Node:
    def __init__(self,name,id,major):
        self.data = {"Name":name,"ID":id,"Major":major}
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,name,id,major):
        new_node = Node(name,id,major)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,key):
        temp = self.head

        if temp and temp.data["Name"] == key:
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data["Name"] == key:
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
            print(temp.data)
            temp = temp.next

llist = LinkedList()

llist.insertAtBegin("Earth",68200609,"CE")
llist.insertAtBegin("Phone",68200243,"CE")
llist.insertAtBegin("Peen",68200584,"CE")
llist.insertAtBegin("Gift",68200124,"CE")
llist.insertAtBegin("Ice",68200268,"CE")
llist.insertAtBegin("Pliw",68200691,"CE")
llist.insertAtBegin("Beam",68200352,"CE")
llist.insertAtBegin("Non",68200164,"CE")
llist.insertAtBegin("Bell",68200269,"CE")
llist.insertAtBegin("Diamond",68200535,"CE")

#llist.printList()

#print("-----------------------------------")
# print("delete Diamond")
llist.deleteNode("Diamond")
#llist.printList()

llist.deleteNode("Ice")
llist.deleteNode("Non")
llist.deleteNode("Bell")
llist.insertAtBegin("Khert","68200624","CE")
print("-----------------------------------")
print("delete Diamond,Ice,Non,Bell add Khert")
llist.printList()