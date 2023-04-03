class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        

class BinarySearchTree(Node):
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            found_place = False
            current_node = self.root
            while not found_place:
                if data <= current_node.data:
                    if current_node.left == None:
                        current_node.left = Node(data)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node.right = Node(data)
                        break
                    else:
                        current_node = current_node.right
                        
