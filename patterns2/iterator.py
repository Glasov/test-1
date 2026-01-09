class Iterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        raise StopIteration
