from Node import Node
        
def DeleteNode(node):
    node.value = node.next.value
    node.next = node.next.next
    
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

head.printList()               
DeleteNode(node5)
print('\nList after removing a node with value 3 is :')
head.printList()         
    