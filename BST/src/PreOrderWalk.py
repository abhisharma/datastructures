from Insert import InsertNode
from Stack import Stack
def PreOrderWalk(root):
    if root != None:
        print(root.value)
        PreOrderWalk(root.left)
        PreOrderWalk(root.right)

def PreOrderWalk_NoRecursion(root):
    s = Stack()
    s.push(root)
    while not s.empty() :
        node = s.pop()
        print(node.value)
        if node.right != None:
            s.push(node.right)
        if node.left != None:
            s.push(node.left)
    

###################################################
root = InsertNode(None, 10)
InsertNode(root, 14)
InsertNode(root, 6)
InsertNode(root, 4)
InsertNode(root, 2)
InsertNode(root, 12)
InsertNode(root, 7)
InsertNode(root, 5)

PreOrderWalk(root)
print(" With No Recursion ")
PreOrderWalk_NoRecursion(root)