
class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for edge in self.graph[vertex]:
                self.graph[edge].remove(vertex)
            del self.graph[vertex]

    def get_vertex(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return None
    
    def get_vertices(self):
        return self.graph.items()
