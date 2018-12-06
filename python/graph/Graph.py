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

    def _print(self, prev : dict, s, t):
        if prev[t] == s:
            print('path: ', s)
            return
        
        self._print(prev, s, prev[t])
        print('path: ', t)

    def bfs(self, s, t):
        visited = set()
        prev = {}
        queue = collections.deque([s])

        while len(queue):
            element = queue.popleft()
            for item in self.adj[element]:

                if item == t:
                    prev[item] = element
                    self._print(prev, s, t)
                    return
                elif item not in visited:
                    prev[item] = element
                    visited.add(item)
                    queue.append(item)

graph = Graph()
graph.insert(1, 2)
graph.insert(1, 4)
graph.insert(1, 5)
graph.insert(2, 3)
graph.insert(2, 4)
graph.insert(2, 5)
graph.insert(3, 4)
graph.insert(3, 5)
graph.insert(3, 6)
graph.insert(4, 5)

print(graph.get_graph())
graph.bfs(1, 6)