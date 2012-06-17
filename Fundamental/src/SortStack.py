import random
from Stack import Stack
def SortStack(s):
    temp = Stack()    
    while not s.empty():
        x = s.pop()
        
        while not temp.empty() and x > temp.peek():
            s.push(temp.pop())           
        temp.push(x)

    return temp

#######################################
q = Stack()
n = 20
for _ in range(n):
    q.push(random.randint(1, n))

q = SortStack(q)
while not q.empty():
    print(q.pop())          
                
        
        