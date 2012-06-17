class Stack:
    def __init__(self):
        self.data = list()
    
    def push(self, value):
        self.data.append(value)
        
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[len(self.data)-1]
    
    def empty(self):
        return len(self.data) == 0