from Insert import InsertNode
def minimum(root):
    while root.left != None:
        root = root.left
    return root

def Successor(node):
    if node.right != None:
        return minimum(node.right)
    else:
        while node.parent != None and node.parent.right == node:
            node = node.parent
        return node.parent
    

###################################################
root = InsertNode(None, 10)
InsertNode(root, 14)
InsertNode(root, 6)
InsertNode(root, 4)
InsertNode(root, 2)
InsertNode(root, 12)
InsertNode(root, 7)
InsertNode(root, 5)

node = minimum(root)

while(node != None):
    print(node.value)
    node = Successor(node)
