# 1. Describe in graphs terminology
# node is a person
# when are two nodes connected (when is there an edge)? when a person has a parent: child -> parent

# 2. Build your graph


# 3. Choose your fighter: DFT, but build a path like our searches do

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, node):
        if node not in self.graph:
            self.graph[node] = set()
        
    def add_edge(self, node1, node2):
        self.graph[node1].add(node2)
        
    def get_neighbors(self, node):
        return self.graph[node]
    
    def size(self):
        return len(self.graph)   
    
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def build_graph(ancestors):
    g = Graph()
    for parent, child in ancestors:
        ## add both vertices because parent might also be a child
        g.add_vertex(parent)
        g.add_vertex(child)
        
        g.add_edge(child, parent)
        
    return g

def earliest_ancestor(ancestors, starting_node):
    g = build_graph(ancestors)
    
    s = Stack()
    visited = set()
    
    s.push([starting_node])
    
    max_path_len = 1
    most_ancient = -1
    
    while s.size():
        current_path = s.pop()
        current_node = current_path[-1]
        
        if len(current_path) > max_path_len or len(current_path) == max_path_len and current_node < most_ancient:
            max_path_len = len(current_path)
            most_ancient = current_node
        
        if current_node not in visited:
            visited.add(current_node)

            parents = g.get_neighbors(current_node)
            
            for parent in parents:
                s.push(current_path + [parent])
    
    return most_ancient