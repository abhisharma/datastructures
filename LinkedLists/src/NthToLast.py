from Node import Node
        
def FindNthToLast(head, n):
    ptr1 = head
    for _ in range(n):
        if ptr1 != None:
            ptr1 = ptr1.next
        else:
            print("List size is less than "+ str(n))
            return -1
        
    ptr2  = head
    while ptr1 != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        
    print(ptr2.value) 
    

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

FindNthToLast(head,4)