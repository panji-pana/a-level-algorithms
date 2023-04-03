import hashlib

class HashTable:
    
    def __init__(self) -> None:
        self.table: dict = {}
    
        
    def _hash(self, unhashedString: str):
        """
        Returns the hashed version of the input using the sha256 algorithm
        """
        
        self.hash = hashlib.new('sha256')
        self.hash.update(unhashedString.encode('utf-8'))
        
        self.hashedString = self.hash.hexdigest()
        return self.hashedString
    
    
    def insert(self,inp: str) -> str:
        """
        Inserts an input into the hash table and returns the hashed equivalent of the input
        """
        
        self.hashedInput = self._hash(inp)
        
        self.table[self.hashedInput] = inp
        return self.hashedInput

    
    def remove(self, inp: str) -> bool:
        """
        Removes the input from the hash table and returns if it has been successful, 
        throws exception if the input is not in the table
        """
        
        if not self.search(inp):
            raise KeyError("Item not in hash table")
        
        self.hashedInput = self._hash(inp)
        
        self.table.pop(self.hashedInput)
        
        self.wasSuccess = not self.search(inp)
        
        return self.wasSuccess
    
    
    def search(self, inp: str) -> bool:
        """
        Returns whether the input is already within the hash table
        """
        
        self.hashedInput = self._hash(inp)
        
        self.isInTable = self.hashedInput in self.table
        return self.isInTable    
    

hashTable = HashTable()
print(hashTable.insert("A"))
print(hashTable.insert("B"))
print(hashTable.insert("C"))
print(hashTable.search("B"))
print(hashTable.remove("B"))
print(hashTable.search("B"))
