class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1
        
    def push(self, item: str) -> int:
        self.top+=1
        self.stack[self.top] = item
        return self.top
    
    def pop(self) -> str:
        if self.top > -1:
            self.top -= 1
            return self.stack[self.top]
        else:
            raise Exception("Stack Underflow")
        
    def peek(self) -> str:
        return self.stack[self.top]