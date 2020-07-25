"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else: 
            print(f'Vertex at position [{vertex_id}] already exists.')
      

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            self.vertices[v1].add(v2)
        except KeyError as error:
            print(str(f'Vertex [{error}] does not exist!'))

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        
        queue.enqueue(starting_vertex)
        
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                
                neighbors = [queue.enqueue(n) for n in self.get_neighbors(current_vertex)]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        
        stack.push(starting_vertex)
        
        while stack.size() > 0:
            current_vertex = stack.pop()
            
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                
                neighbors = [stack.push(n) for n in self.get_neighbors(current_vertex)]

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
            
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            
            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return visited
        
            for n in neighbors:
                self.dft_recursive(n, visited)
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        
        path = [starting_vertex]
        queue.enqueue(path)
        
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_vertex = current_path[-1]
            
            if current_vertex == destination_vertex:
                return current_path
            
            if current_vertex not in visited:
                visited.add(current_vertex)   
                neighbors = self.get_neighbors(current_vertex)
                
                for n in neighbors:
                    n_path = list(current_path)
                    n_path.append(n)
                    
                    queue.enqueue(n_path)                        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        
        path = [starting_vertex]
        stack.push(path)
        
        while stack.size():
            current_path = stack.pop()
            current_vertex = current_path[-1]
            
            if current_vertex == destination_vertex:
                return current_path
            
            if current_vertex not in visited:
                visited.add(current_vertex)
                
                neighbors = self.get_neighbors(current_vertex)
                
                for n in neighbors:
                    n_path = list(current_path)
                    n_path.append(n)
                    
                    stack.push(n_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        #define my base case
        #work through stack, adding vertices to the list to return until I reach the destination vertex

        if path == visited == None:
            path = [starting_vertex]
            visited = set()
      
   
        if starting_vertex not in visited:
            visited.add(starting_vertex)            
            
            if starting_vertex == destination_vertex:
                return path
            
            for n in self.get_neighbors(starting_vertex):
                n_path = list(path)
                n_path.append(n)
            
                ret = self.dfs_recursive(n, destination_vertex, visited, n_path)
        
                if ret:
                    return ret
        
        
                
       
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    ## start test addition
    graph.add_vertex(7)
    ## end test addition
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    ## start test addition
    graph.add_edge(8, 6)
    ## end test addition

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
