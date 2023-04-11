from weighted_graph import Graph

global infinity
infinity = float('inf')

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
    

if __name__ == "__main__":
    import dijkstra as d
    dijkstra = d.Dijkstra()

    dijkstra.create_graph('A','B','C','D','E','x')

    dijkstra.add_children('A',['B',10],['C',7])
    dijkstra.add_children('B',['A',10],['E',4],['D',4])
    dijkstra.add_children('C',['A',7],['E',3])
    dijkstra.add_children('D',['B',4],['x',1])
    dijkstra.add_children('E',['B',4],['C',3],['x',6])
    dijkstra.add_children('x',['D',1],['E',6])

    path = dijkstra.traverse('A','x')
    print(path)
