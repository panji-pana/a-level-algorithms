class Node:
    def __init__(self,  node: str) -> None:
        self.node = node
        self.visited = False
        self.distance = float('inf')
        self.g = float('inf')
        self.h = 0
        self.f = self.g + self.h
        self.previous = None
        self.children = []
        
    def updateF(self) -> None:
        self.f = self.g + self.h


class Child:
    def __init__(self, data: str, weight: int) -> None:
        self.node = data
        self.weight = weight


class Graph(Node, Child):
    """
    This class includes the modules needed to create and fill
    a weighted graph easily
    """
    
    def __init__(self) -> None:
        self.graph = {}
        
    def create_graph(self, *nodes: str) -> None:
        """Add all nodes to graph"""
        for node in nodes:
            self.graph[node] = Node(node)
            
        
    def add_children(self, parent: str, *children: list[str,int]) -> None:
        """Add all the children of the node (parent) of the graph"""
        for child in children:
            child_class = Child(child[0],child[1])
            self.graph[parent].children.append(child_class)

        