import collections

class Graph:
    def __init__(self):
        self.adj = {}

    def insert(self, s, t):
        if s in self.adj.keys():
            self.adj[s].append(t)
        else:
            self.adj[s] = [t]

        if t in self.adj.keys():
            self.adj[t].append(s)
        else:
            self.adj[t] = [s]

    def get_graph(self):
        return self.adj

    def bfs(self, s, t):
        pass

graph = Graph()
graph.insert(1, 2)
graph.insert(1, 3)
graph.insert(1, 4)
graph.insert(1, 5)
graph.insert(2, 3)
graph.insert(2, 4)
graph.insert(2, 5)
graph.insert(3, 4)
graph.insert(3, 5)
graph.insert(4, 5)

print(graph.get_graph())