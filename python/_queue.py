class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.front = 0
        self.back = -1
        
    def enqueue(self, item: str):
        self.back += 1
        self.queue[self.back] = item
        
    def dequeue(self):
        self.front += 1
        if self.front > self.back:
            raise Exception("Queue underflow")
        
    def peek(self):
        return self.queue[self.front]