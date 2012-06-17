from Node import Node
def Insert(root, parent, value, dir):
    if root == None:
        node = Node(parent, None, None, value)
        if parent != None:
            if dir:
                parent.left = node
            else:
                parent.right = node
                
        return node
    else:
        if value <= root.value:
            node = Insert(root.left, root, value, True)
        else:
            node = Insert(root.right, root, value, False)
            
    return node

def InsertNode(root, value):
    return Insert(root, None, value, None)
    