def displayNodeReverse(self):
        nodes = []
        self.nav = self.tail
        while(self.nav is not None):
            nodes.append(self.nav.data)
            self.nav = self.nav.prev
        print("Double Linked-List :", nodes)
    def mySearch(self, what):
        search1 = self.head
        search2 = self.tail
        while(search1 and search2):
            if(search1.data == what):
                print(f"Found {what} by head to tail")
                break
            if(search1 == self.tail and search2 == self.head):
                print("Not Found")
                break
            search1 = search1.next
            search2 = search2.prev
    def deleteNode(self,target):
        self.nav = self.head
        while(self.nav != None):
            if self.nav.data == target:
                if self.nav.prev:
                    self.nav.next = self.nav.next
                if self.nav.next:
                    self.nav.prev = self.nav.prev
                if self.nav == self.head:
                    self.head = self.nav.next
                return
            self.nav = self.nav.next