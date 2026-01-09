class Handler:
    def __init__(self, nxt=None):
        self.next = nxt
    def handle(self, req):
        if self.next: return self.next.handle(req)
