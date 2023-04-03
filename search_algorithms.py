class SearchAlgorithms:
    def __init__(self) -> None:
        pass
    
    def binary(self,arr, aim):
        self.upper = len(arr)-1
        self.lower = 0
        self.mid = (self.upper-self.lower)//2
        
        while self.upper != self.lower:
            if arr[self.mid] > aim:
                self.upper = self.mid
            elif arr[self.mid] < aim:
                self.lower = self.mid
            else:
                return self.mid
        
            self.mid = (self.upper+self.lower)//2
            
        return self.lower
    
    def linear(self, arr, aim):
        for i in range(len(arr)):
            if arr[i] == aim:
                return i