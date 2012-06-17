class Bag:
    def __init__(self):
        self.data = list()
    
    def add(self, value):
        self.data.append(value)
    
    def empty(self):
        return len(self.data) == 0
