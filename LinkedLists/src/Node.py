class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def printList(self):
        head = self
        while head != None:
            print(head.value,end='\t')
            head = head.next
        