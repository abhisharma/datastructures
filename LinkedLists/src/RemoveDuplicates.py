from Node import Node

def RemoveDuplicates(head):
    Set = set()
    cur = head
    previous = None
    while cur != None:
        if cur.value not in Set:
            Set.add(cur.value)
            previous = cur
        else:
            previous.next = cur.next
        cur = cur.next
    
def RemoveDuplicates_NoExtraBuffer(head):
    cur = head
    previous = None
    
    while cur != None:
        ptr = head
        duplicate = False
        while ptr != cur:
            if ptr.value == cur.value:
                duplicate = True
                break
            ptr = ptr.next
        if duplicate:
            previous.next = cur.next
        else:
            previous = cur
        cur = cur.next 
    
    
#############################################    
node1 = Node(2, None) 
node2 = Node(6, node1)
node3 = Node(4, node2)
node4 = Node(5, node3)
node5 = Node(3, node4)
node6 = Node(2, node5)
node7 = Node(1, node6)
node8 = Node(1, node7)
node9 = Node(5, node8)
head = Node(4, node9)

print("########## Test 1 ###############")
head.printList()            
RemoveDuplicates(head)
print('\nList after removing duplicates is :')
head.printList()       
    
#############################################    
node1 = Node(2, None) 
node2 = Node(6, node1)
node3 = Node(4, node2)
node4 = Node(5, node3)
node5 = Node(3, node4)
node6 = Node(2, node5)
node7 = Node(1, node6)
node8 = Node(1, node7)
node9 = Node(5, node8)
head = Node(4, node9)

print("\n########## Test 2 ###############")
head.printList()              
RemoveDuplicates_NoExtraBuffer(head)
print('\nList after removing duplicates is :')
head.printList() 