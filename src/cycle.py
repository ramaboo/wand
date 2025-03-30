class Cycle:
    def __init__(self, list):
        self.list = list
        self.index = 0
        
    def next_item(self):
        self.index = (self.index + 1) % len(self.list)
        return self.list[self.index]
        
    def previous_item(self):
        self.index = (self.index - 1) % len(self.list)
        return self.list[self.index]
        
    def current_item(self):
        return self.list[self.index]
        