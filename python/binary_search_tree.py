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
                        
    def preorder(self, node = None, aim = None):
        if node == None:
            node = self.root 
        if node == aim:
            return node
            
        print(node.data)
        if node.left != None:
            self.preorder(node.left)
        if node.right != None:
            self.preorder(node.right)
            
    def inorder(self, node = None, aim=None):      
        if node == None:
            node = self.root
        if node == aim:
            return node
            
        if node.left != None:
            self.inorder(node.left)
        print(node.data)
        if node.right != None:
            self.inorder(node.right)
    
    def postorder(self, node = None, aim=None):      
        if node == None:
            node = self.root
        if node == aim:
            return node
            
        if node.left != None:
            self.postorder(node.left)
        if node.right != None:
            self.postorder(node.right) 
        print(node.data) 
 
 
        
    
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bst.insert(10)

    print("Preorder pre-delete")
    bst.preorder()
    print("\nInorder pre-delete")
    bst.inorder()
    
    
    
    

