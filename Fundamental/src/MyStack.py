from Queue import Queue
class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        
    def push(self, value):
        self.queue1.enqueue(value)
        
    def pop(self):
        while not self.queue1.empty():
            value = self.queue1.dequeue()
            if not self.queue1.empty():
                self.queue2.enqueue(value)
                   
        while not self.queue2.empty():
            self.queue1.enqueue(self.queue2.dequeue())
            
        return value
    
    def empty(self):
        return self.queue1.empty()
        
        
#######################################
q = MyStack()
q.push(5)
q.push(1)
q.push("hello")
q.push(789)
q.push("another")


while not q.empty():
    print(q.pop())