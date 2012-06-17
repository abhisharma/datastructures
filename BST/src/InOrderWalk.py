from Insert import InsertNode
from Stack import Stack

def InOrderWalk(root):
    if root != None:
        InOrderWalk(root.left)
        print(root.value)
        InOrderWalk(root.right)

def InOrderWalk_NoRecursion(root):
    s = Stack()
    s.push(root)
    while not s.empty() :
        node = s.peek()
        if node.left != None:
            s.push(node.left)
            continue

        node = s.pop()
        while node != None:
            print(node.value)
            if node.right == None:
                if not s.empty():
                    node = s.pop()
                else:
                    break
            else:
                s.push(node.right)
                break

    
###################################################
root = InsertNode(None, 10)
InsertNode(root, 14)
InsertNode(root, 6)
InsertNode(root, 4)
InsertNode(root, 2)
InsertNode(root, 12)
InsertNode(root, 7)
InsertNode(root, 5)

InOrderWalk(root)
print(" With No Recursion ")
InOrderWalk_NoRecursion(root)