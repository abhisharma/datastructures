from Node import Node

def Add(head1, head2):
    previousNode = None
    head = None
    carry = 0
    while head1 != None or head2 != None:
        value = 0
        if head1 != None:
            value = head1.value
        if head2 != None:
            value += head2.value
        
        sum = value + carry
        carry = 0
        if sum > 9:
            carry = 1
            sum = sum % 10
        node = Node(sum, None)
        if previousNode != None:
            previousNode.next = node
        else:
            head = node
        previousNode = node
            
        if head1 != None:
            head1 = head1.next
        if head2 != None:
            head2 = head2.next
            
    if carry != 0:
        node = Node(carry, None)
        previousNode.next = node
        
    return head
                

#############################################   
node1 = Node(1, None)
node2 = Node(5, node1)
head1 = Node(4, node2)

node3 = Node(9, None)
node4 = Node(9, node3)
head2 = Node(9, node4)


print("########## Test 1 ###############")
head1.printList()  
print("\n")           
head2.printList()   
newhead = Add(head1, head2)
print("\n")
newhead.printList()        

node1 = Node(9, None)
node2 = Node(7, node1)
head1 = Node(3, node2)

node3 = Node(9, None)
node4 = Node(9, node3)
node5 = Node(5, node4)
head2 = Node(9, node5)


print("\n########## Test 2 ###############")
head1.printList()     
print("\n")          
head2.printList()  
print("\n")
newhead = Add(head1, head2)
newhead.printList()       