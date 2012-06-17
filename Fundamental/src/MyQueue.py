from Stack import Stack
class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, value):
        self.stack1.push(value)
        
    def dequeue(self):
        if not self.stack2.empty():
            return self.stack2.pop()
        
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
                       
        return self.stack2.pop()
    
    def empty(self):
        return self.stack1.empty()
        
        
#######################################
q = MyQueue()
q.enqueue(5)
q.enqueue("hello")
q.enqueue(2)
q.enqueue("another")
q.enqueue(6)


while not q.empty():
    print(q.dequeue())