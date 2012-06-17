from Node import Node

time = 0
def DFS(nodes):
    for node in nodes:
        if node.color == 'WHITE':
            DFSVisit(node)
    
def DFSVisit(node):
    global time
    
    node.color = 'GRAY'
    time = time + 1
    node.d = time
    
    for adjNode in node.adj:
        if adjNode.color == 'WHITE':
            adjNode.p = node
            DFSVisit(adjNode)
    node.color = 'BLACK'
    time = time + 1
    node.f = time
    print('Finished visiting node ' + node.value + ', d time =  ' + str(node.d), ', f time =  ' + str(node.f),  end='\n') 

    
 
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

DFS([n1, n2, n3, n4, n5, n6, n7, n8])

