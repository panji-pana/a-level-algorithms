import copy

class QuickSort:
    def __init__(self, inputtedArray) -> None:
        self.array = inputtedArray
        
    def quickSort(self, low:int =0, high: int|None =None):
        if high == None:
            high = len(self.array)-1
            
        if low < high:
            partitionIndex = self.partition(low,high)
            
            self.quickSort(low,partitionIndex-1)
            self.quickSort(partitionIndex+1,high)
            
        return self.array
            
    def partition(self, low, high):
        pivot = self.array[high]
        
        index_smaller = low-1
        
        for i in range(low,high):
            if self.array[i] < pivot:
                index_smaller+=1
                
                temp = self.array[index_smaller]
                self.array[index_smaller] = self.array[i]
                self.array[i] = temp
                
        temp = self.array[index_smaller + 1]
        self.array[index_smaller + 1] = self.array[high]
        self.array[high] = temp
        
        return index_smaller+1

class SortingAlgorithms(QuickSort):
    def __init__(self, inputtedArray) -> None:
        self.array = inputtedArray
    
    def bubbleSort(self)-> list:
        thisArray = copy.copy(self.array)
        sorted = False
        
        while not sorted: 
            sorted = True
            
            for i in range(len(thisArray)-1):
                if thisArray[i] > thisArray[i+1]:
                    temp = thisArray[i]
                    
                    thisArray[i] = thisArray[i+1]
                    thisArray[i+1] = temp
                    
                    sorted = False
                    
        return thisArray
                    
    def insertionSort(self) -> list:
        thisArray = copy.copy(self.array)
        
        for i in range(1,len(thisArray)):
            j = i
            while j>0 and thisArray[j-1] > thisArray[j]:
                    temp = thisArray[j]
                    thisArray[j] = thisArray[j-1]
                    thisArray[j-1] = temp
                    
                    j-=1
                    
        return thisArray
                
    def mergeSort(self, thisArray=None) -> list:
        if thisArray == None:
            thisArray = copy.copy(self.array)
        
        if len(thisArray) > 1:
            mid = len(thisArray)//2
            leftArray = thisArray[:mid]
            rightArray = thisArray[mid:]
            
            thisArray[:mid] = self.mergeSort(leftArray)
            thisArray[mid:] = self.mergeSort(rightArray)
            
            i = j = k = 0
            
            while i < len(leftArray) and j < len(rightArray):
                if leftArray[i] < rightArray[j]:
                    thisArray[k] = leftArray[i]
                    i+=1
                else:
                    thisArray[k] = rightArray[j]
                    j+=1
                k+=1
            
            while i < len(leftArray):
                thisArray[k] = leftArray[i]
                i+=1
                k+=1
                
            while j < len(rightArray):
                thisArray[k] = rightArray[j]
                j+=1
                k+=1
                
        return thisArray

        