from Stack import Stack
class Tower:
    def __init__(self,index):
        self.stack = Stack()
        self.index = index
        
    def addDisk(self, disk):
        if self.stack.empty() or self.stack.peek() > disk:
            self.stack.push(disk)
        else:
            print("Error in adding disk " + str(disk) + " to tower "+ str(self.index))
        
    def removeDisk(self):
        if not self.stack.empty():
            return self.stack.pop()
        else:
            return -1    
        
    def printContents(self):
        s = Stack()
        print("Contents of Stack " + str(self.index))
        while not self.stack.empty():
            disk = self.stack.pop()
            print(disk)
            s.push(disk)
            
        while not s.empty():
            self.stack.push(s.pop())
        
    def moveOneDisk(self, tower):
        disk = self.removeDisk()
        if disk != -1:
            tower.addDisk(disk)
            print("Moved disk "+ str(disk) + " from tower " + str(self.index) + " to tower " + str(tower.index))
    
    # This is the important one    
    def moveDisks(self, destTower, bufferTower, n):
        if n > 0:
            self.moveDisks(bufferTower, destTower, n-1)
            self.moveOneDisk(destTower)
            bufferTower.moveDisks(destTower, self, n-1)
        
##################################################################################   
        
t1 = Tower(1)
t2 = Tower(2)
t3 = Tower(3)
n = 10

for i in range(n):
    t1.addDisk(n-i)

t1.printContents()
t2.printContents()
t3.printContents()

t1.moveDisks(t3,t2,n)

t1.printContents()
t2.printContents()
t3.printContents()
        
    
    
    