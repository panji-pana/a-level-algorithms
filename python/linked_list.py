class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.pointer = None
        
        
class LinkedList(Node):
    def __init__(self, head = None) -> None:
        self.head = head
        
        
    def append(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            return True
        current_node = self.head
        
        while True:
            if current_node.pointer == None:
                current_node.pointer = Node(new_data)
                break 
            
            else:
                current_node = current_node.pointer
                
    
    def remove(self, data):
        current_node = self.head
        while True:
            next_node = current_node.pointer
            if next_node == None:
                return False
            elif next_node.data == data:
                current_node.pointer = next_node.pointer
            else:
                current_node = next_node    
                
    
    def traverse(self):
        current_node = self.head
        while True:
            print(current_node.data)
            if current_node.pointer == None:
                break
            current_node = current_node.pointer
            
            
            
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(40)
    linked_list.append(60)
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(50)
    linked_list.append(90)
    linked_list.append(70)
    linked_list.append(30)
    linked_list.append(80)
    linked_list.traverse()
    print("")
    linked_list.remove(10)
    linked_list.remove(20)
    linked_list.traverse()
    
            