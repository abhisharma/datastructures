from Node import Node
from Queue import Queue

def BFS(root):
    root.d = 0
    root.color = 'GRAY'
    
    q = Queue()
    q.enqueue(root)
    
    while not q.empty():
        node = q.dequeue()
        print('Visiting node ' + node.value + ', distance from source is ' + str(node.d), end='\n') 
        
        for adjNode in node.adj:
            if adjNode.color == 'WHITE':
                adjNode.color = 'GRAY'
                adjNode.p = node
                adjNode.d = node.d + 1
                q.enqueue(adjNode)
        
        node.color = 'black'
    
 
###########################
n1 = Node('r')
n2 = Node('s')
n3 = Node('t')
n4 = Node('u')
n5 = Node('v')
n6 = Node('w')
n7 = Node('x')
n8 = Node('y')

n1.adj = [n2, n5]
n2.adj = [n1, n6]
n3.adj = [n4, n6, n7]
n4.adj = [n3, n7, n8]
n5.adj = [n1]
n6.adj = [n2, n3, n7]
n7.adj = [n3, n4, n6, n8]
n8.adj = [n7, n4]

BFS(n2)

