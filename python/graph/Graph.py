from collections import *

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.dfs_found = False

    def insert(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def get_graph(self):
        return self.adj

    def _print(self, prev : dict, s, t):
        if prev[t] == s:
            print('path: ', t)
            return
        
        self._print(prev, s, prev[t])
        print('path: ', t)

    def bfs(self, s, t):
        visited = set()
        prev = {}
        queue = deque([s])

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
    
    def _recursive_dfs(self, visited, prev, s, t):
        if self.dfs_found:
            return

        visited.add(s)

        for node in self.adj[s]:

            if node in visited:
                continue
            
            prev[node] = s
            if node == t:
                self.dfs_found = True
            
            self._recursive_dfs(visited, prev, node, t)

    def dfs(self, s, t):
        visited = set()
        prev = {}

        self._recursive_dfs(visited, prev, s, t)

        self._print(prev, s, t)

graph = Graph()
graph.insert(1, 2)
graph.insert(1, 3)
graph.insert(2, 4)
graph.insert(2, 5)
graph.insert(3, 4)
graph.insert(4, 6)
graph.insert(5, 6)
graph.insert(6, 7)

print(graph.get_graph())
# graph.bfs(1, 7)

graph.dfs(1, 7)