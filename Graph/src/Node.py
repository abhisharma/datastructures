class Node:
    def __init__(self, value ='', color='WHITE', d=-1, p=None, adj=None):
        self.color = color
        self.d = d
        self.p = p
        self.value = value
        self.adj = adj
        self.f = -1 # Only for DFS
        
        