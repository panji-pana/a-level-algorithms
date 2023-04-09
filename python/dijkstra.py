global infinity
infinity = float('inf')


class Node:
    def __init__(self,  node: str) -> None:
        self.node = node
        self.visited = False
        self.distance = infinity
        self.previous = None
        self.children = []


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


class Dijkstra(Graph):
    """
    This module contains the method to traverse through
    a graph using Dijkstra's pathfinding algorithm
    """
    
    def __init__(self) -> None:
        super().__init__()


    def traverse(self, start: str, goal: str) -> list[str]:
        """Traverse through graph using Dijkstra's shortest path algorithm"""
        
        # set start node
        self.graph[start].distance = 0
        
        # for each node in the graph:
        for node in self.graph:
            # find the node with the shortest distance that has not been visited
            shortest_distance = infinity
            shortest_node = None
            
            for inner_node in self.graph:
                if self.graph[inner_node].distance < shortest_distance and not self.graph[inner_node].visited:
                    shortest_distance = self.graph[inner_node].distance
                    shortest_node = inner_node
            
            # for each node that has not been visited:
            for child in self.graph[node].children:
                if not self.graph[child.node].visited:
                    # calculate the distance from the start
                    new_distance = self.graph[node].distance + child.weight
                    
                    # if the distance from the start is lower than the current distance:
                    if new_distance < self.graph[child.node].distance:
                        # set the shortest distance to the newly calculated distance
                        shortest_distance = new_distance
                        
                        # set the previous node to the current node
                        self.graph[child.node].distance = new_distance
                        self.graph[child.node].previous = node
                        
            # set visited attribute to be true
            self.graph[node].visited = True
            
        # Start from the goal node
        path = []
        path.append(self.graph[goal].node)
        previous = None
        # Repeat until start node is reached 
        while previous is not start:
            # Add the previous node to the start of a list
            previous = self.graph[path[len(path)-1]].previous
            path.append(self.graph[previous].node)
        
        # Output the list    
        return path
    
