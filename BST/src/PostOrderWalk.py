from Insert import InsertNode
from Stack import Stack
def PostOrderWalk(root):
    if root != None:
        PostOrderWalk(root.left)
        PostOrderWalk(root.right)
        print(root.value)

def PostOrderWalk_NoRecursion(root):
    s = Stack()
    s.push(root)
    while not s.empty() :
        node = s.peek()
        if node.right != None:
            s.push(node.right)
            continue
        if node.left != None:
            s.push(node.left)
            continue
        
        if root.left != None:
            s.push(root.left)
            root = root.left
        else:
            break
       
    
    while not s.empty():
        print(s.pop().value) 
###################################################
root = InsertNode(None, 10)
InsertNode(root, 14)
InsertNode(root, 6)
InsertNode(root, 4)
InsertNode(root, 2)
InsertNode(root, 12)
InsertNode(root, 7)
InsertNode(root, 5)

PostOrderWalk(root)
print(" With No Recursion ")
PostOrderWalk_NoRecursion(root)