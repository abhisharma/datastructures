from Stack import Stack
sentinal = 9999999999999999
class StackWithMin:
    def __init__(self):
        self.stack = Stack()
        self.minstack = Stack()
    
    def push(self, value):
        self.stack.push(value)
        if value < self.min():
            self.minstack.push(value)
        
    def pop(self):
        if self.stack.peek() ==  self.minstack.peek():
            self.minstack.pop()
        return self.stack.pop()
    
    def peek(self):
        return self.stack.peek()
    
    def empty(self):
        return self.stack.empty()
    
    def min(self):
        if self.minstack.empty():
            return sentinal
        else:
            return self.minstack.peek()
        
#########################################
s = StackWithMin()
s.push(8)
s.push(7)
s.push(6)
s.push(20)
s.push(1)
s.push(2)
s.push(0)
s.push(4)

while not s.empty():
    print("Min is " + str(s.min()))
    s.pop()