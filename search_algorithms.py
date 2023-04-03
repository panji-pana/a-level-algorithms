class SearchAlgorithms:
    def __init__(self) -> None:
        pass
    
    def binary(self,arr, aim):
        upper = len(arr)-1
        lower = 0
        mid = (upper-lower)//2
        
        while upper != lower:
            if arr[mid] > aim:
                upper = mid
            elif arr[mid] < aim:
                lower = mid
            else:
                return mid
        
            mid = (upper+lower)//2
            
        return lower
    
    def linear(self, arr, aim):
        for i in range(len(arr)):
            if arr[i] == aim:
                return i