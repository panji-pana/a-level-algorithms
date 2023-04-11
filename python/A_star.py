from weighted_graph import Graph
import string
import dijkstra

global infinity
infinity = float('inf')

class A_star(Graph):
    def __init__(self) -> None:
        super().__init__()
        
    def traverse(self, start: str, goal: str) -> list:
        
        # Until the goal node has been visited:
        while not self.graph[goal].visited:
            # Find the node with the lowest "f" value that has not been visited
            lowestF = infinity
            lowestNode = None
            
            for node in self.graph:
                if self.graph[node].f < lowestF and not self.graph[node].visited:
                    lowestNode = node
                    lowestF = self.graph[node].f
                    
            # For each connected node that has not been visited:        
            for child in self.graph[lowestNode].children:
                # i. Calculate the relative distance from the start by adding the edge value and the heuristic
                relative_distance = self.graph[child.node].h + child.weight
                
                #ii. If the distance from the start plus the heuristic is lower than the currently recorded value for "f":
                if relative_distance < self.graph[child.node].f:
                    # 1. Set the "f" value of the connected node to the newly calculated distance
                    self.graph[child.node].f = relative_distance
                    
					# 2. Set the previous node to the current node
                    self.graph[child.node].previous = lowestNode
                    
            # set the current node as visited
            self.graph[lowestNode].visited = True
            
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
                    
        
        
if __name__ == "__main__":
    graph = A_star()
    graph_dijkstra = dijkstra.Dijkstra() # to compare paths for validation
    
    graph.create_graph('A','B','C','D','E','F','Z')
    
    graph.add_children('A',['B',9],['C',4],['D',7])
    graph.add_children('B',['E',11])
    graph.add_children('C',['E',17],['F',12])
    graph.add_children('D',['F',14])
    graph.add_children('E',['Z',5])
    graph.add_children('F',['Z',9])
    
    graph_dijkstra.graph = graph.graph
    
    graph.graph['A'].g = 0
    graph.graph['A'].h = 21
    graph.graph['B'].h = 14
    graph.graph['C'].h = 18
    graph.graph['D'].h = 18
    graph.graph['E'].h = 5
    graph.graph['F'].h = 8
    
    
    for letter in list(string.ascii_uppercase)[:5]:
        graph.graph[letter].updateF()
        
    path = graph.traverse('A','Z')
    print(path)
    
    path = graph_dijkstra.traverse('A','Z')
    print(path)
    
    
    